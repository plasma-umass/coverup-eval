from pathlib import Path
import json
from coverup.logreader import parse_log_raw
import litellm


def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--suite', choices=['good', '1_0'], default='good',
                    help='suite of modules to compare')

    ap.add_argument('--config', type=str, help='specify a (non-default) configuration to use')
    return ap.parse_args()


def cost_of(log_content: str):
    cost = 0

    for ts, ctx, content in parse_log_raw(log_content):
        if content.startswith("{"):
            j = json.loads(content)
            if 'choices' in j:
                cost += litellm.completion_cost(j)

    return cost

if __name__ == '__main__':
    args = parse_args()

    total = 0

    path = Path('output') / (args.suite + (f".{args.config}" if args.config else ""))
    if not path.exists():
        print(f"{path} doesn't exist")

    else:
        for file in path.glob("*/coverup-log-*"):
            if '.' in file.name: # "foobar.failed" and such
                continue

            cost = cost_of(file.read_text())
            print(f"{str(file.relative_to(path)):<55} $ {cost:6.2f}")
            total += cost

        print(f"\nTotal cost: $ {total:6.2f}")
