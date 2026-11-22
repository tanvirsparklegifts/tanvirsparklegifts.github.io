# GitHub Career Roadmap

Owner: Md Tanvir Ahammed Tonmoy  
Positioning: AI Systems Architect  
Audience: international engineering teams, open-source maintainers, recruiters, and technical partners.

## Current portfolio audit (2026-11-23)

Four public repositories were visible during the audit:

1. `tanvirsparklegifts.github.io` — personal portfolio and architecture notes.
2. `aetherium-vault` — browser cryptography UI prototype.
3. `aero-x-protocol` — Go-based distributed orchestration simulation.
4. `elite-axis-engine` — FastAPI foundation in development.

The repository descriptions and READMEs currently overstate some capabilities. Treat status labels as evidence-based: prototype, simulation, in development, or published demo. Do not describe a prototype as production-ready or claim security properties that have not been independently tested.

## Priority 0 — Profile credibility

- Create the special GitHub profile repository named exactly `tanvirsparklegifts`.
- Copy `docs/PROFILE_README_TEMPLATE.md` into that repository as `README.md`.
- Add a concise professional bio and a portfolio link to GitHub account settings.
- Pin the best four repositories after the profile README is published.
- Keep project status, supported features, setup instructions, and limitations accurate.

## Priority 1 — Make each project reviewable

### AERO-X Protocol
- Fix and standardize the package layout (the current tree contains a suspicious nested `pkg/pkg/nexus` path).
- Add unit tests for telemetry updates, heartbeat expiry, and queue priority.
- Add context cancellation and bounded queue behavior.
- Add GitHub Actions for `go test ./...`, `go vet ./...`, and formatting checks.
- Document that the current runtime is a simulation, not flight-control or safety-certified software.

### Aetherium Vault
- Replace the fixed PBKDF2 salt with a fresh cryptographically random salt per encryption operation and store it with the ciphertext.
- Use a fresh, unique 96-bit IV for every AES-GCM encryption and store it with the ciphertext.
- Add input validation, error handling, and tests for round-trip encryption, wrong passphrases, and tampered ciphertext.
- Remove claims such as hardware enclave, zero-knowledge proof implementation, or validated sub-microsecond performance unless separately implemented and measured.
- Document the threat model and explicitly state that the current project is a browser-side prototype.

### EliteAxis Global Engine
- Expand the README with setup, configuration, API examples, architecture, and current limitations.
- Verify package structure and imports; remove accidental nested directories if confirmed safe.
- Add tests for authentication, authorization, configuration, and error paths.
- Add CI for linting and tests.
- Avoid describing health responses as proof that the service is secure or production-ready.

### Portfolio repository
- Keep the public website synchronized with the project repositories.
- Add concise case studies with problem, architecture, implemented scope, demo, test evidence, and next steps.
- Keep a downloadable CV accurate and current.

## Priority 2 — Open-source participation

- Make small, high-quality contributions to projects in AI tooling, Python/FastAPI, Go, developer tooling, and documentation.
- Read each project's contribution guide and open issues before coding.
- Prefer reproducible bug reports, tests, documentation fixes, and narrowly scoped pull requests.
- Track every contribution with links to issues, PRs, review outcomes, and lessons learned.

## Priority 3 — Career and partnership readiness

- Maintain an English-first profile and repository documentation.
- Prepare a one-page CV and a concise architecture case-study portfolio.
- Make a clear collaboration contact route available.
- For each partnership, define the scope, ownership, deliverables, payment terms, IP rights, and responsibilities in writing.

## Weekly operating standard

- One meaningful repository improvement or reviewed open-source contribution.
- One tested and documented deliverable, not a low-value repository created merely to increase repository count.
- Review profile links, pinned projects, issue backlog, and project status.
- Record evidence: merged PRs, releases, tests, demos, and feedback.

## Definition of done

A project is career-ready when a new reviewer can understand what it does, run it, inspect the architecture, see tests or known limitations, and identify the author's actual contribution without relying on unsupported claims.
