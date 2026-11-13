# Sprint Log

## Sprint 1 — Week 3: Project planning and repository organisation

### Sprint goal
Prepare a clear project portfolio and organise the documentation needed to guide the next development stage.

### Sprint backlog

| Issue | Task | Status |
|---|---|---|
| #1 | Prepare the project README and problem statement | Completed |
| #2 | Document functional and non-functional requirements | Completed |
| #3 | Prepare user stories and acceptance criteria | Completed |
| #4 | Organise the docs and src folders | Completed |
| #5 | Review the proposed technology stack | Completed |

### Daily stand-up notes
- **Stand-up 1:** Reviewed the project problem, intended users and repository structure. The main risk was keeping the scope realistic for the assignment.
- **Stand-up 2:** Completed the core project documents and identified testing and prototype work as the next steps.

### Sprint review
The repository now contains a project overview, problem statement, requirements, user stories and a source-code placeholder. The documents describe a prototype that flags unusual records for human review.

### Retrospective
- **What went well:** The project scope and documentation are organised in one repository.
- **What was difficult:** Deciding how much implementation is realistic within the available time.
- **What to improve:** Link each requirement to a test and keep the prototype small and demonstrable.

## Sprint 2 — Week 4: Testing, CI and portfolio deployment

### Sprint goal
Apply the Week 4 lab practices to the Better-Brighter portfolio: create project-specific tests, run them through GitHub Actions and publish the static project information page.

### Sprint backlog

| Issue | Task | Status |
|---|---|---|
| #6 | Add a small Python validation prototype | Completed |
| #7 | Add automated unit tests for project functions | Completed |
| #8 | Configure GitHub Actions to run pytest | Completed |
| #9 | Prepare a static GitHub Pages project page | Completed |
| #10 | Verify the latest workflow and published page | Pending GitHub run and Pages configuration |

### Sprint review
A small demonstration implementation and automated tests have been added. The workflow is configured to run tests on pushes and pull requests. The static portfolio page is prepared for GitHub Pages.

### Retrospective
- **What went well:** The project now has a small testable code sample and a repeatable CI workflow.
- **What was difficult:** Separating the Week 4 study-planner example from the actual anomaly-detection project.
- **What to improve:** Confirm the workflow result and GitHub Pages deployment in the repository before reporting a green status or live URL.

## Important record-keeping note
The Week 4 starter ZIP contains a study-planner example with its own tests. Its test results are not Better-Brighter results. Only the tests in this repository should be used when reporting this project's test status.
