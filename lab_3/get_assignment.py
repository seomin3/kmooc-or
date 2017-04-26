import gachon_autograder_client as g_autograder

THE_TEAMLABIO_ID = 'kjahyeon'
PASSWORD = 'tiger098'
ASSIGNMENT_NAME = 'nb_test'

g_autograder.get_assignment(THE_TEAMLABIO_ID, PASSWORD, ASSIGNMENT_NAME)
