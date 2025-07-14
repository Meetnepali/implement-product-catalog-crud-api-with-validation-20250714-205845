# Guidance for Task

This codebase is a partially implemented FastAPI SaaS user activity event logging API. Your goal is to complete and enhance the event logging endpoints so authenticated users can POST their activity events (with robust validation and custom metadata) and GET their own paginated, filterable activity log. Data must be securely persisted using SQLAlchemy async models. Payloads need Pydantic validation. APIs must have proper error responses and well-documented OpenAPI schemas. Authentication is required and currently simulated.

## What You Should Do
- Implement the missing logic and validations so users can securely POST activity events and GET their own logs (with pagination and filtering).
- Ensure endpoints are placed in the correct router, and use async/await route handlers and FastAPI dependency injection.
- Make sure request and response schemas are robust, documented, and errors are handled consistently.
- Validate input data using Pydantic, including custom metadata fields.
- Use SQLAlchemy transactions to safeguard data integrity.
- Route authentication is handled via a custom header scheme (see app/auth.py).
- Write or enhance tests to assert request input errors and a successful retrieval of events by an authenticated user.

## Key Requirements
- Only allow actions for authenticated users (via the Authorization header).
- POST endpoint must validate fields and attempt to store new events in the database.
- GET endpoint must return paginated and filterable event logs, belonging to the authenticated user only.
- Your solution should leverage async SQLAlchemy sessions and FastAPI best practices.
- All error responses must use clearly defined schemas and correct HTTP status codes.
- Routes should be placed in the dedicated router (see app/routers/events.py).

## Verifying Your Solution
- Review and run the included tests in tests/test_events.py to check that input validation is enforced and authenticated retrieval works.
- Ensure your implementation passes these tests and provides all required OpenAPI docs and error handling.
- Code must be reasonable to complete and verify in 15-20 minutes for an intermediate developer.

## Notes
- Focus is on robust API structure, validation, error handling, and correct async use (not just simple CRUD).
- Don’t worry about advanced authentication schemes—use provided stubs.
- No need to add project setup instructions in this document.
