from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)

    def get_inviter_reason(self):
        qs = self.group_set
        import pdb; pdb.set_trace()
        return qs .first()#.members.first().invite_reason


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

