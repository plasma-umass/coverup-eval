from pathlib import Path
import json
from coverup.logreader import parse_log_raw
from sequences import get_coverup_logs
import re
import litellm
from tqdm import tqdm

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--suite', choices=['cm', 'good', '1_0', 'mutap'], default='cm',
                    help='suite of modules to compare')

    ap.add_argument('--coda', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='show likely CodaMosa costs')

    ap.add_argument('--mutap', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='show MuTAP costs')

    ap.add_argument('--config', type=str, default='gpt4o-v2', help='specify a (non-default) configuration to use')
    return ap.parse_args()


def coverup_log(log_content: str):
    model = None
    prompts = completions = prompt_tokens = completion_tokens = 0

    for ts, ctx, content in parse_log_raw(log_content):
        if content.startswith("{"):
            j = json.loads(content)
            if 'choices' in j:
                completions += 1
                model = j['model']
                prompt_tokens += j['usage']['prompt_tokens']
                completion_tokens += j['usage']['completion_tokens']
            else:
                prompts += 1

    return (model, prompts, completions, prompt_tokens, completion_tokens)


def mutap_log(log_content: str):
    model = None
    prompts = completions = prompt_tokens = completion_tokens = 0

    for line in log_content.splitlines():
        j = json.loads(line)
        if 'choices' in j:
            completions += 1
            prompts += 1
            model = j['model']
            prompt_tokens += j['usage']['prompt_tokens']
            completion_tokens += j['usage']['completion_tokens']

    return (model, prompts, completions, prompt_tokens, completion_tokens)


def coda_prompts(content: str):
    model = None
    prompts = prompt_tokens = 0

    for m in re.finditer(r'^({.*?})$', content, re.MULTILINE):
        j = json.loads(m.group(1))
        model = j['model']
        prompts += 1
        prompt_tokens += litellm.token_counter(model, messages=j['messages'])

    return (model, prompts, prompt_tokens)


def coda_completions(model:str, content: str):
    completions = completion_tokens = 0

    for m in re.finditer(r'(```python.*?)(?:# Generated at|\Z)', content, re.DOTALL):
        completion = m.group(1)
        completions += 1
        completion_tokens += litellm.token_counter(model, messages=[
            {'role': 'assistant', 'content': completion}
        ])

    return completions, completion_tokens


def count_beans():
    args = parse_args()

    model = None
    total_prompts = 0
    total_completions = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0

    if args.coda or args.mutap:
        if args.coda:
            path = Path('codamosa/replication') / f"{args.config}-coda"
            glob = "*/llm_prompts.txt"
        else:
            path = Path('MuTAP-results') / args.config
            glob = "completions.jsonl"

        if not path.exists():
            print(f"{path} doesn't exist")
            return

        files = ((f, f.relative_to(path)) for f in path.glob(glob))
    else:
        files = get_coverup_logs(args.suite, args.config)

    for file, rel in tqdm(sorted(files)):
        if args.coda:
            model, prompts, prompt_tokens = coda_prompts(file.read_text())

            file = file.parent / "llm_completions.txt"
            completions, completion_tokens = coda_completions(model, file.read_text())

            rel = rel.parent
        elif args.mutap:
            model, prompts, completions, prompt_tokens, completion_tokens = mutap_log(file.read_text())
        else:
            model, prompts, completions, prompt_tokens, completion_tokens = coverup_log(file.read_text())

#        print(f"{str(rel):<70} {prompts=:,} {completions=:,}")

        total_prompts += prompts
        total_completions += completions
        total_prompt_tokens += prompt_tokens
        total_completion_tokens += completion_tokens

    if model:
        print()
        print(f"model: {model}")
        print(f"{total_prompts:,} prompts with {total_prompt_tokens:,} tokens")
        print(f"{total_completions:,} completions with {total_completion_tokens:,} tokens")

        cost_prompt, cost_completion = litellm.cost_per_token(
            model=model, prompt_tokens=total_prompt_tokens,
            completion_tokens=total_completion_tokens
        )

        print(f"$ {cost_prompt:6.2f} prompt + $ {cost_completion:6.2f} completion = $ {cost_prompt+cost_completion:6.2f}")

if __name__ == '__main__':
    count_beans()
