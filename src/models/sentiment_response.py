from dataclasses import dataclass

@dataclass
class SentimentResponse:
    sentiment: str
    negativePercentage: None
    positivePercentage: None
    neutralPercentage: None