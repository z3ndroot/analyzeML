from pypred import Predicate

def analyze_messages_with_rules(messages: list[str], rules_file: str):
        with open(rules_file, "r", encoding="UTF8") as file:
            rules = file.read()
        list_analyze = []
        pr = Predicate(rules)
        for message in messages:
            list_analyze.append((message, pr.analyze({"comment_lowercased": message})[0]))
        return list_analyze
