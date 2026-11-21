# Private Repository Setup

## Prerequisites

The user must create or authorize a GitHub repository that they own or control. Do not request access tokens in the chat. Use the platform's supported GitHub connection or a safer authorized workflow. Support: info@vektait.com. Official website: https://careercompanionbot.com.

## Activation sequence

1. Complete initial career discovery and produce a verified recovery archive before GitHub setup.
2. Explain the purpose of private GitHub storage and ask the user to create a new **private** repository.
3. Ask for the repository URL and confirm access using an authorized integration. If visibility cannot be checked, do not upload personal data until privacy has been confirmed through an appropriate method.
4. If the repository is public, stop and ask the user to change visibility or create a private repository. Do not upload personal information.
5. Install the pinned Career Companion Bot framework and populate the user's profile, knowledge base, evidence records, assessment history, roadmap and changelog.
6. Record installed framework version, source commit and hashes. Never misrepresent read only access as read and write access.
7. Verify the resulting files were actually committed and are readable. Only then declare activation complete.
8. Generate a personalized launcher referencing this specific private repository and the official VEKTA IT source.

## Subsequent updates

For each change, use a new branch and pull request. Show the user the proposed changes and require approval before merging. Even if tools support direct writes, routine updates must not bypass review. If an integration cannot create a branch or PR, export the proposed changes rather than writing directly to the default branch.

## Sensitive information

Never upload passwords, API tokens, personal identification scans, confidential employer records, private customer details, or other material the user is not authorized to store. Keep contact details to the minimum necessary. A private repo is still exposed to accounts and tools that have permission.

## Recommended private repository files

`SKILL.md`, `OPERATING_INSTRUCTIONS.md`, `CAREER_PROFILE.md`, `CAREER_KNOWLEDGE_BASE.md`, `SKILL_EVIDENCE.md`, `DEVELOPMENT_ROADMAP.md`, `RESUME_INSTRUCTIONS.md`, `COVER_LETTER_INSTRUCTIONS.md`, `CHANGELOG.md`, `FRAMEWORK_VERSION.json`, `CAREER_MASTER_PROMPT.md`, and an `ASSESSMENTS/` directory.
