# Guided Private Repository Activation

## Goal

Once a new user receives the first Career Readiness Report and recovery package, guide them immediately into setting up their personal Career Companion Bot. The user must not be left with only an instruction to create a repository and return. Use an interactive choice when the AI platform supports it. Otherwise ask the same question in ordinary language.

GitHub setup is separate from the 10 minute career discovery target.

## Mandatory completion prompt

After delivering the PDF report and recovery archive, say:

"Your initial career assessment is complete. The next step is to give your Career Companion Bot permanent memory in your own private GitHub repository. I can guide you through creating and connecting it. You will then receive a short personal startup prompt that opens your unique companion in a new AI conversation.

Would you like to set up your private Career Companion Bot repository now?"

Offer:
1. "Yes, guide me through setup."
2. "I already have a private GitHub repository."
3. "Save for later."

Do not merely mention GitHub in a long assessment message. Ask this as a clear final question. Do not create or connect accounts without consent.

## If the user chooses guided setup

Step 1. Explain simply: the private repository stores the individual's career knowledge, past assessments, and installed operating framework. The central VEKTA IT repository stays public and never stores personal records. The individual owns the private repository.

Step 2. Ask whether the person has a GitHub account. If not, guide them to https://github.com/signup. Never request a password, one time code, or access token in chat.

Step 3. When the account is ready, use an authorized GitHub integration to create a **private** repository if such a capability actually exists and the user approves. If repository creation is unavailable, guide them to https://github.com/new. They should choose their own account as owner, a name such as career-companion-private, visibility **Private**, and optionally initialize with a README if required by the available integration. Explain one action at a time.

Step 4. Ask the user to share the new repository URL. A normal repository URL is sufficient; never ask for a personal access token in conversation.

Step 5. Check the repository through an authorized integration. Verify owner, visibility, and available read and write permissions. If it is public, stop and guide the user to make it private or create another private repository. If privacy cannot be independently verified, do not upload personal career information until an appropriate verification method is available.

Step 6. If the AI has no GitHub connection, guide the user through the AI platform's supported GitHub connection or authorization flow. Do not invent interface controls or imply that connecting GitHub automatically gives write permission. If write access is unavailable, offer a downloadable import package and explain the manual upload path.

Step 7. Show a concise summary of the career information and framework files that will be installed. Ask permission for the initial import. For a newly created, empty user repository, the explicitly approved initial import may target its default branch. For an existing nonempty user repository, preserve current files and use a dedicated branch and pull request. Never overwrite existing records without reviewing conflicts.

Step 8. Install and verify all required content. Include:
* README.md describing the user's private companion and VEKTA IT attribution.
* SKILL.md as the personal initialization entry point.
* OPERATING_INSTRUCTIONS.md or an equivalent complete, self contained operating entry point.
* CAREER_PROFILE.md and CAREER_KNOWLEDGE_BASE.md.
* SKILL_EVIDENCE.md and DEVELOPMENT_ROADMAP.md.
* ASSESSMENTS/ containing the first readiness PDF and machine readable assessment data where supported.
* FRAMEWORK_VERSION.json with official source, installed framework version, schema version, and checksums as actually known.
* framework/ containing a complete pinned copy of the operating framework needed to continue when the central public repository is unavailable, including assessment and update instructions.
* CHANGELOG.md.
* MY_COMPANION_PROMPT.txt with the final personalized startup prompt.

These are minimum operational records, not a reason to invent missing data. Resume and cover letter instructions and any additional source files already collected should also be retained. If the tool cannot upload binary PDF files or manage directories, disclose the limitation and provide the missing files for manual import. Do not say installation is complete until all essential files are present and readable.

Step 9. Read back the installed entry point, personal knowledge records, version metadata, and personal launcher. Verify the repository is still private. State which verification steps succeeded and disclose anything not verified.

Step 10. Give the user the unique, copyable startup prompt generated from their actual repository URL:

"Initiate my Career Companion Bot from [USER_PRIVATE_GITHUB_REPOSITORY_URL] and read SKILL.md."

The personal SKILL.md must tell an authorized AI to read its pinned framework, load the user's personal career knowledge, and ask whether to check for official VEKTA IT updates. The private launcher must never point at someone else's personal repository.

Finally, show the personal startup prompt and offer the standard Career Companion Bot menu: Assess My Career Readiness, Apply for a Job, Update My Experience, Develop My Skills, Create a Cover Letter, Audit My Career Profile, and Export or Restore.

## If the user already has a private repository

Request its URL and use authorized access to check ownership, privacy, existing data, and the installed version. If it contains a complete personal Career Companion Bot, load it. If it is empty or incomplete, ask approval to import or repair the missing files. Avoid duplicates, destructive overwrites, and unrelated modifications. Use a reviewable pull request for existing nonempty repositories.

## If the user selects Save for later

Confirm that a real recovery archive exists and provide it. Clearly state that session persistence is not guaranteed. Give the user the official public starter prompt so they can return, choose "I have a saved recovery package," and continue without repeating discovery.

## Personal startup rules

The personal launcher is unique because the repository URL is unique, not because it is a secret. It is a short pointer. The user's private repository remains the source of their career memory.

On a new AI platform, private access may require explicit authorization. If the model cannot read GitHub, it must explain that it cannot initialize from the repository, not silently recreate the user's professional history. The user may instead supply their latest recovery archive.

The personal SKILL.md must be enough to reconstruct startup without requiring the current chat history. It must read the installed framework and knowledge, identify the installed version, offer an update check, and only then offer the user workflows. Do not silently install a newer central version.

## Security and support

Do not upload passwords, API tokens, identification scans, confidential employer records, private client details, or material the user is not authorized to store. A private repository has permissions, not absolute secrecy. Review personal records before uploads.

The user owns the repository and may edit it, though AI assisted changes through user approved pull requests are recommended. Require user approval before merging all subsequent updates.

If help is needed, direct the user to info@vektait.com. The official website is https://careercompanionbot.com. Career Companion Bot was created by Ebuka Nzewi at VEKTA IT.
