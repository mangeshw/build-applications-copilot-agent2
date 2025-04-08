from bson import ObjectId
from octofit_tracker.serializers import ObjectIdField

# Test ObjectIdField
field = ObjectIdField()

# Test to_representation
object_id = ObjectId()
representation = field.to_representation(object_id)
print("Representation:", representation)

# Test to_internal_value
internal_value = field.to_internal_value(representation)
print("Internal Value:", internal_value)

assert str(object_id) == representation, "to_representation failed"
assert object_id == internal_value, "to_internal_value failed"

print("ObjectIdField tests passed!")
