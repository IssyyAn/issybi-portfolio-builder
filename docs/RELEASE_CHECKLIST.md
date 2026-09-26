# Release Checklist

## 1. Upload the repository

- Create a public GitHub repository named `issybi-portfolio-builder`.
- Upload the contents of this release folder, preserving all paths.
- Confirm `README.md`, `LICENSE`, `docs/`, `submission/`, `.agents/`, and `plugins/` are present.
- Enable GitHub Issues for support.
- Create a `v1.0.0` release and attach the two ZIP bundles from `dist/`.

## 2. Replace URL placeholders

In `submission/listing.md`, replace `OWNER` with the GitHub username or organisation. Confirm the website, support, privacy, and terms URLs open without signing in.

## 3. Test the exact package

- Add the GitHub repository as a plugin marketplace or test the local checkout.
- Run every `PB-SUB` test in a fresh chat.
- Record evidence in `Portfolio_Builder_Skill_Test_Plan_v1.0.xlsx`.
- Do not submit until all eight cases pass and the full release rule in `docs/TESTING.md` is satisfied.

## 4. Prepare OpenAI Platform access

- Use the organisation that will own the public plugin.
- Ensure the submitter has **Apps Management: Write** permission.
- Complete individual verification for a personal publisher name, or business verification for the Issy BI business name.
- Make sure the verified identity matches the public listing and policy pages.

## 5. Create the submission

- Open the OpenAI plugin submission portal.
- Choose **Skills only**.
- Use the listing copy in `submission/listing.md`.
- Upload `dist/data-portfolio-builder-skill-v1.0.0.zip` on the Skills tab. If the portal requests the complete portable package instead, use `dist/issybi-portfolio-builder-plugin-v1.0.0.zip`.
- Add the starter prompts from `submission/starter-prompts.md`.
- Add the five positive and three negative cases from `submission/test-cases.md`.
- Select only countries where the publisher, support process, and legal terms are ready.
- Add `submission/release-notes.md`.

## 6. Review and attest

- Confirm the package contains no secrets, personal data, private URLs, or unsupported claims.
- Confirm the listing, skill, prompts, tests, availability, privacy policy, and terms are accurate.
- Complete the portal’s policy attestations yourself.
- Submit for review.

## 7. Publish after approval

Approval does not publish automatically. Return to the portal, choose the approved version, and publish it. Then verify the listing and starter prompts in the universal Plugins Directory.

