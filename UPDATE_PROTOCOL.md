# Official Update Protocol

## Distribution

The public VEKTA IT repository is the official distribution channel. Users retain a pinned framework copy in their private repository. Framework updates and personal career data updates are independent.

## Version awareness

Use semantic release versions. The installed version record contains the origin repository, source commit, release identifier, content checksums and schema compatibility. Fetch an official release only after the user elects to check for updates. Do not automatically replace the installed version.

## Authenticity and integrity

A manifest with file hashes can detect accidental changes when checked independently. It cannot by itself prove publisher identity. Signed release provenance or attestations require external verification by an appropriate tool and trusted identity. If such a tool is missing, disclose the verification limit. Public access cannot prevent third parties from copying the framework or creating unofficial bots. Never call an unofficial copy official merely because it refers to this repository.

## Upgrade procedure

1. Ask to check for updates.
2. Retrieve official metadata from the configured repository and confirm the version is newer and schema compatible.
3. Show an understandable summary of differences and any migration risks.
4. Ask whether to prepare the upgrade.
5. Create a pull request changing only framework owned files or safe migration metadata. Never overwrite personal career records or historical assessments.
6. Wait for explicit user approval before merge.
7. Verify installed version after approved merge.
8. Preserve last known working version and recovery export.

## Failure behavior

If the central repository is unavailable, operate using the installed pinned framework. If personal repository access is unavailable, do not claim persistence. If compatibility or authenticity cannot be confirmed, do not install the release. Never automatically downgrade or delete private career information.
