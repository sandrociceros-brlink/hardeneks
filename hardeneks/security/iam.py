from ..resources import NamespacedResources
from ..report import print_role_table


def restrict_wildcard_for_roles(resources: NamespacedResources):
    offenders = []

    for role in resources.roles:
        for rule in role.rules:
            if "*" in rule.verbs:
                offenders.append(role)
            if "*" in rule.resources:
                offenders.append(role)

    if offenders:
        print_role_table(
            offenders,
            "Roles should not have '*' in Verbs or Resources",
            "Role",
        )
    return offenders