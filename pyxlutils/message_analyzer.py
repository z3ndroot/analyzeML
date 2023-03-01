from pypred import Predicate

def analyze_messages_with_rules(messages: list[str], rules_file: str):
        with open(rules_file, "r", encoding="UTF8") as file:
            rules = file.read()
        list_analyze = []
        pr = Predicate(rules)
        for message in messages:
            list_analyze.append((message, pr.evaluate({"comment_lowercased": message.lower()})))
        return list_analyze


def analyze_meta_with_rules(meta: list[dict], rules_file: str):
    with open(rules_file, "r", encoding="UTF8") as file:
        rules = file.read()
    list_analyze = []
    pr = Predicate(rules)
    for data in meta:
        list_analyze.append((data["comment_lowercased"], pr.evaluate(data)))
    return list_analyze