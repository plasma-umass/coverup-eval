from pathlib import Path
from sequences import parse_args, parse_log, get_sequences
from datetime import datetime
import llm_utils

MODEL='gpt-4-1106-preview'
args = parse_args()

_token_encoding_cache = dict()
def count_tokens(text: str, model = MODEL):
    """Counts the number of tokens in a chat completion request."""
    import tiktoken

    if not (encoding := _token_encoding_cache.get(model)):
        encoding = _token_encoding_cache[model] = tiktoken.encoding_for_model(model)

    return len(encoding.encode(text))

total_time = 0
total_serial_time = 0
total_tokens = 0
for file in sorted((Path('output') / (args.modules + (f".{args.config}" if args.config else ""))).glob(args.logs)):
    if '.' in file.name: # "foobar.failed" and such
        continue

    if args.skip and args.skip in str(file):
        continue

    log_content = file.read_text()

    file_time = 0
    start = end = None
    for ts, ev, details, content in parse_log(log_content):
        if ev == 'startup':
            if start:
#                print(f"start: {start} end: {end}")
                diff = datetime.fromisoformat(end) - datetime.fromisoformat(start)
                file_time += diff.total_seconds()

            start = end = ts
            continue

        # include ? just in case... not all are actually responses/prompts.
        if ev in ('P', 'C', 'F', 'S', 'R', 'U', '?'):
            total_tokens += count_tokens(content)

        end = ts

    if start:
#        print(f"start: {start} end: {end}")
        diff = datetime.fromisoformat(end) - datetime.fromisoformat(start)
        file_time += diff.total_seconds()

    serial_time = 0
    for _, _, ts in get_sequences(log_content):
        diff = datetime.fromisoformat(ts[-1]) - datetime.fromisoformat(ts[0])
#        print(ts[0], ts[-1], diff.total_seconds())
        serial_time += diff.total_seconds()

    print(f"{str(file):60} {file_time:.0f}s {serial_time:.0f}s")
    total_time += file_time
    total_serial_time += serial_time

print('')
print(f"Total time:  {total_time}s, {total_time/3600:.1f}h")
print(f"Serial time: {total_serial_time}s, {total_serial_time/3600:.1f}h, {total_serial_time/total_time:.1f}x")
print(f"Tokens:      {total_tokens}  {llm_utils.calculate_cost(total_tokens, 0, MODEL):.1f}")
