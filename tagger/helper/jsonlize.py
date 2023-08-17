import jsonlines
from fire import Fire


def main(input_file, output_file):
    lines = []
    with open(input_file, 'r', encoding='utf8') as f:
        for i, line in enumerate(f.readlines()):
            lines.append({'id': i, 'text': line.strip(), 'labels': []})
    with jsonlines.open(output_file, 'w') as writer:
        writer.write_all(lines)


file_dir = 'F:\code\ReviewAdvisor-main\\tagger\sample.txt'
output_files = 'out.jsonl'
main(file_dir, output_files)
# if __name__ == '__main__':
#     Fire(main)
