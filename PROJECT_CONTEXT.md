# Career Companion Bot Maintainer Context

This is the human maintained state and design decision record for the public Career Companion Bot project. This document is for developers and authorized AI collaborators, not personal career onboarding. Update this record when a pull request introduces a material architectural decision, changes a product workflow, or completes a roadmap item.

## Identity

Official name: Career Companion Bot.
Creator: Ebuka Nzewi at VEKTA IT.
Official source: https://github.com/Seempleman/career-companion-bot
Website: https://careercompanionbot.com
Support: info@vektait.com
Maintainer repository owner: Seempleman.

## Mission and philosophy

Career Companion Bot discovers, understands, evaluates, preserves and helps develop a person's real career experience throughout life. It is not just a resume generator. Never invent work history, credentials, skills, results, or industry standards.

VEKTA IT maintains the public and inspectable framework. Every user owns an independent private GitHub repository holding personal professional memory, assessment history, and a pinned copy of the framework. The user controls approvals and access. Neither the framework nor the private assistant should depend entirely on the other to remain useful.

## Current architecture

The entire official framework is publicly readable from this repository. A one sentence starter prompt asks an AI to read START_HERE.md. The entry point asks for permission to activate before loading the full framework.

After consent, the assistant asks whether the person has an existing private companion repository, is new, or has a saved recovery package.

New users enter adaptive discovery. Initial discovery targets 10 minutes or less, up to 10 progress stages, a resume first approach, and only the questions needed to identify real evidence. The AI offers to proceed when evidence is sufficient.

The assessment uses validated occupations, credible occupational references, current postings when research is available, hybrid skill evidence, and transparent scoring. It produces a one page career readiness report with confidence and limitations, plus a portable recovery package. Missing documentation is not proof that a person lacks a skill.

After the assessment, the assistant must offer interactive private GitHub activation: create or connect a private repository, obtain authorized access, verify privacy, import career records and the pinned operating framework, read back installed files, and generate a personal launcher pointing to the private repository and SKILL.md. It can also save the recovery package for later. Normal personal record updates use reviewable pull requests and user approved merges.

The private personalized startup prompt is different from the universal public starter prompt. Each user's private repository and career memory are independent.

## Style decisions

Use clear professional English, no contractions, no decorative punctuation, concise questions, and no fabricated claims. The initial greeting begins with a waving symbol. Keep product promotion out of users' resumes and cover letters.

## Official framework governance

The public official repository can be read and copied. Only authorized repository collaborators can publish official versions. Public access does not restrict unofficial bots from reading it. Verify source and content integrity within available capabilities and never claim a signature check that was not performed.

Framework updates are optional, versioned, and never installed into personal assistants without approval. A local pinned copy allows continuity if the public source is unavailable. Framework version and release status must come from RELEASE_MANIFEST.json, not assumptions.

## Automation and checkpoint workflow

A GitHub Actions workflow on main pushes generates a machine readable PROJECT_CHECKPOINT.json and a readable PROJECT_CHECKPOINT.md in the separate project-checkpoints branch. It records source commit SHA, version and release status, recent commit subjects, repository inventory, and this maintained design context. The source commit is the freshness proof: the maintainer assistant must compare it to main before using the digest. The source documents remain authoritative.

## Current status and unresolved work

The official manifest identifies version 1.0.0 as candidate_not_published. This is not yet a formally signed, immutable release.

The public one sentence starter, user consent, initial onboarding and post assessment GitHub guidance have been tested or incorporated following a fresh Claude test. The fresh test produced a report and a recovery package. Full private repository activation and successful personal launcher use in a new AI conversation have not yet been verified end to end.

The GitHub repository has a checksum validation workflow for public framework files. Branch protection or rulesets, signed releases, and release attestations have not been confirmed active. Do not present them as completed.

The public website URL is reserved in documentation; no website implementation has been confirmed.

The project is publicly readable but has no selected redistribution license as of this checkpoint.

## Next suggested engineering work

1. Test and improve first time private GitHub installation, including recovery completeness and cross provider startup from a personal SKILL.md.
2. Verify the checkpoint automation runs on main, can write to the project-checkpoints branch, and produces source commit aligned outputs.
3. Develop real automated onboarding tests across AI providers with no hidden conversation context.
4. Configure official release governance, branch protections and a signed release process.
5. Choose a public reuse and redistribution license before general promotion.
6. Reconcile the changelog and finalize a first release after testing.
7. Build the website later. It is not required for the GitHub based product.

## Maintainer session rules

The maintainer uses MAINTAINER_PROMPT.txt to start a fresh AI chat, checks project-checkpoints against main, reads the relevant actual files, identifies verified versus proposed features, and offers a concise current state plus next development choices. All edits are proposed on a feature branch through a pull request. Never merge without user approval and never modify user owned private CareerOS repositories while updating the universal framework.
