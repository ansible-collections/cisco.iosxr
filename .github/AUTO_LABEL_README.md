# Auto-Label Functionality

This document describes the auto-labeling functionality implemented for the `cisco.iosxr` collection.

## Overview

The auto-label workflow automatically adds labels to Pull Requests and Issues based on the information provided in the PR and Issue templates. This helps with:

- **Better organization**: Issues and PRs are automatically categorized
- **Faster triage**: Maintainers can quickly identify the type of change
- **Workflow automation**: Labels can trigger other workflows or notifications
- **Metrics and reporting**: Better tracking of work types across the collection

## How It Works

### For Pull Requests

The workflow parses the PR template's "Type of Change" section and adds labels based on checked boxes:

| Template Checkbox | Label Added |
|------------------|-------------|
| Bug fix | `bug` |
| New feature | `enhancement` |
| New module | `new-module` |
| Breaking change | `breaking-change` |
| Documentation update | `documentation` |
| Test update | `tests` |
| Refactoring | `refactor` |
| Collection release | `release` |
| CI maintenance | `ci` |
| Workflow maintenance | `workflow` |
| Configuration change | `config` |

Additionally, the workflow analyzes the "Component Name" section to add component-specific labels:
- If component mentions "plugin" → adds `plugin` label
- If component starts with "iosxr_" → adds `module` label

### For Issues

The workflow parses the Issue template's "Select the relevant components" section and adds labels based on checked boxes:

| Template Checkbox | Label Added |
|------------------|-------------|
| Module | `module` |
| Action Plugin | `plugin` |
| Connection Plugin (cliconf) | `plugin` |
| Terminal Plugin | `plugin` |
| Netconf Plugin | `plugin` |
| Module Utils | `module-utils` |
| Documentation | `documentation` |
| Integration Tests | `tests` |
| Unit Tests | `tests` |
| Collection Release | `release` |
| CI Maintenance | `ci` |
| Workflow Maintenance | `workflow` |

Additionally:
- Bug reports (with "Bug Summary" field) automatically get the `bug` label
- Feature requests (with "Feature Summary" field) automatically get the `enhancement` label

## Workflow File

The auto-labeling is implemented in `.github/workflows/auto_label.yml` and uses:
- `actions/github-script@v7` for parsing template content and adding labels
- Triggers on PR/Issue opened, edited, or synchronized events

## Required Labels

Make sure the following labels exist in your repository (they should be created automatically, but you can verify in Settings → Labels):

- `bug`
- `enhancement`
- `new-module`
- `breaking-change`
- `documentation`
- `tests`
- `refactor`
- `release`
- `ci`
- `workflow`
- `config`
- `module`
- `plugin`
- `module-utils`

## Example

When a PR is opened with the following in the "Type of Change" section:

```markdown
## Type of Change
- [x] Bug fix (non-breaking change which fixes an issue)
- [x] Documentation update
```

The workflow will automatically add:
- `bug`
- `documentation`

## Future Enhancements

Potential improvements that could be added:

1. **Automatic assignment**: Assign PRs to specific maintainers based on component
2. **Milestone assignment**: Link PRs to milestones based on labels
3. **Notification routing**: Notify specific teams based on component labels
4. **Label validation**: Ensure required labels are present before merging
5. **Label cleanup**: Remove outdated labels when PRs are updated

## Troubleshooting

If labels are not being added:

1. Check that the workflow file exists at `.github/workflows/auto_label.yml`
2. Verify the PR/Issue body contains the template sections in the expected format
3. Check GitHub Actions logs for any errors
4. Ensure the labels exist in the repository
5. Verify the checkbox format matches exactly (case-insensitive): `- [x] Label text`

## Related Files

- `.github/workflows/auto_label.yml` - Main workflow file
- `.github/PULL_REQUEST_TEMPLATE.md` - PR template
- `.github/ISSUE_TEMPLATE/bug_report.yml` - Bug report template
- `.github/ISSUE_TEMPLATE/feature_request.yml` - Feature request template

