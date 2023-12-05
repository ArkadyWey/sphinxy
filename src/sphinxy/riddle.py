from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Checks whether answer given matches correct answer.

        Args:
            answer (str): 
                The answer given to the riddle.

        Returns:
            bool: 
                Whether answer was same as correct answer or not.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Provides the nect letter of the answer to the riddle question.

        Yields:
            Iterator[str]: The next letter of the riddle question.
        """
        yield from iter(self.answer)
