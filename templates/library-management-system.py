from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional
import uuid

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    copies_available: int

@dataclass
class Member:
    name: str
    member_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Loan:
    book: Book
    member: Member
    issue_date: datetime
    due_date: datetime
    returned: bool = False

    def mark_returned(self):
        self.returned = True
        self.book.copies_available += 1

@dataclass
class Library:
    books: List[Book] = field(default_factory=list)
    members: List[Member] = field(default_factory=list)
    loans: List[Loan] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books.append(book)

    def register_member(self, member: Member):
        self.members.append(member)

    def find_book_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def issue_book(self, title: str, member: Member) -> Optional[Loan]:
        book = self.find_book_by_title(title)
        if book and book.copies_available > 0:
            loan = Loan(
                book=book,
                member=member,
                issue_date=datetime.now(),
                due_date=datetime.now() + timedelta(days=14)
            )
            book.copies_available -= 1
            self.loans.append(loan)
            return loan
        else:
            print(f"Book '{title}' is not available.")
            return None

    def return_book(self, loan: Loan):
        loan.mark_returned()

# ==== Example Usage ====

# Setup
library = Library()

# Add books
library.add_book(Book("1984", "George Orwell", "12345", 3))
library.add_book(Book("Brave New World", "Aldous Huxley", "67890", 2))

# Register member
alice = Member("Alice")
library.register_member(alice)

# Issue book
loan = library.issue_book("1984", alice)
if loan:
    print(f"Book '{loan.book.title}' issued to {loan.member.name} until {loan.due_date.date()}")

# Return book
library.return_book(loan)
print(f"Book '{loan.book.title}' returned by {loan.member.name}")




"""
Design Problems :

 Hotel Room Booking System
 Car Rental Management
 E-Commerce Order System
 Banking System
 Student-Course Registration System
 Event Management System
 Invoice Generator
 Pet Adoption Center
 Online Quiz Platform
 Simple Game: Inventory + Player Stats



"""