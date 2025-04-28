from pydantic import BaseModel, Field, field_validator
from typing import List


class Author(BaseModel):
    name: str
    birth_year: int
    nationality: str

    # Meta class or settings class
    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True


class Book(BaseModel):
    title: str
    publication_year: int
    author: Author  # Nested Author Model
    genres: List[str] = []  # List of genres (e.g. ["Fantasy", "Adventure"])

    @field_validator("genres")
    def validate_genres(cls, value):
        allowed_genres = {"novel", "poem"}
        invalid_genres = [genre for genre in value if genre not in allowed_genres]
        if invalid_genres:
            raise ValueError(
                f"Invalid genres: {', '.join(invalid_genres)}. Only 'novel' and 'poem' are allowed"
            )
        return value

    # Meta class or settings class
    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True


# Example Uses
author_data = {"name": "J.K. Rowling", "birth_year": 1965, "nationality": "British"}

book_data_valid = {
    "title": "Harry Potter and the Sorcerer's Stone",
    "publication_year": 1997,
    "author": author_data,
    "genres": ["novel"],  # valid genres
}

book_data_invalid = {
    "title": "Some Other Book",
    "publication_year": 2020,
    "author": author_data,
    "genres": ["novel", "sci-fi"],  # invalid genres
}

# Creating a valid book instance
book_valid = Book(**book_data_valid)
print(book_valid)

# Creating an invalid book instance (will raise a validation error)
try:
    book_invalid = Book(**book_data_invalid)
except ValueError as err:
    print(f"Validation Error: {err}")
