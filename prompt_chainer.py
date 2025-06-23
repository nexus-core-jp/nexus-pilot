import os
from typing import List, Tuple


class PromptChainer:
    """Simple prompt chaining logic for Nexus-Pilot."""

    def __init__(self,
                 base_path: str = "base.txt",
                 suggestion_path: str = "suggestion.txt",
                 meta_eval_path: str = "meta_eval.txt") -> None:
        root = os.path.dirname(os.path.abspath(__file__))
        self.base_prompt = self._load(os.path.join(root, base_path))
        self.suggestion_prompt = self._load(os.path.join(root, suggestion_path))
        self.meta_eval_prompt = self._load(os.path.join(root, meta_eval_path))

    @staticmethod
    def _load(path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def _apply_base(self, message: str) -> str:
        return f"{self.base_prompt}\nUser request: {message}"

    def generate_suggestions(self, message: str) -> List[str]:
        """Create three simple suggestions based on the message."""
        processed = self._apply_base(message)
        suggestions = []
        for i in range(3):
            suggestions.append(
                f"{processed}\n{self.suggestion_prompt}\nSuggestion {i+1}: {message} option {i+1}.")
        return suggestions

    def select_best(self, suggestions: List[str]) -> Tuple[str, str]:
        """Select the best suggestion with a trivial heuristic."""
        # choose the suggestion with the most characters
        chosen = max(suggestions, key=len)
        rationale = f"{self.meta_eval_prompt}\nThe option with the most detail was selected."
        return chosen, rationale

    def run(self, message: str) -> str:
        suggestions = self.generate_suggestions(message)
        best, _ = self.select_best(suggestions)
        # strip prompts from the output, leaving only the final suggestion sentence
        # last line after 'Suggestion {n}:'
        final_line = best.split("Suggestion")[-1]
        final_text = final_line.split(":", 1)[-1].strip()
        return final_text
