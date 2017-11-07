# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class WorkspaceRealTimeStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkspaceRealTimeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        """
        super(WorkspaceRealTimeStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid,}

    def get(self):
        """
        Constructs a WorkspaceRealTimeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        return WorkspaceRealTimeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __call__(self):
        """
        Constructs a WorkspaceRealTimeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        return WorkspaceRealTimeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsList>'


class WorkspaceRealTimeStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkspaceRealTimeStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsPage
        """
        super(WorkspaceRealTimeStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkspaceRealTimeStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        return WorkspaceRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsPage>'


class WorkspaceRealTimeStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkspaceRealTimeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        super(WorkspaceRealTimeStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid,}
        self._uri = '/Workspaces/{workspace_sid}/RealTimeStatistics'.format(**self._solution)

    def fetch(self, task_channel=values.unset):
        """
        Fetch a WorkspaceRealTimeStatisticsInstance

        :param unicode task_channel: The task_channel

        :returns: Fetched WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        params = values.of({'TaskChannel': task_channel,})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkspaceRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsContext {}>'.format(context)


class WorkspaceRealTimeStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid):
        """
        Initialize the WorkspaceRealTimeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        super(WorkspaceRealTimeStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'activity_statistics': payload['activity_statistics'],
            'longest_task_waiting_age': deserialize.integer(payload['longest_task_waiting_age']),
            'tasks_by_priority': payload['tasks_by_priority'],
            'tasks_by_status': payload['tasks_by_status'],
            'total_tasks': deserialize.integer(payload['total_tasks']),
            'total_workers': deserialize.integer(payload['total_workers']),
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid,}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkspaceRealTimeStatisticsContext for this WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        if self._context is None:
            self._context = WorkspaceRealTimeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def activity_statistics(self):
        """
        :returns: The activity_statistics
        :rtype: dict
        """
        return self._properties['activity_statistics']

    @property
    def longest_task_waiting_age(self):
        """
        :returns: The longest_task_waiting_age
        :rtype: unicode
        """
        return self._properties['longest_task_waiting_age']

    @property
    def tasks_by_priority(self):
        """
        :returns: The tasks_by_priority
        :rtype: dict
        """
        return self._properties['tasks_by_priority']

    @property
    def tasks_by_status(self):
        """
        :returns: The tasks_by_status
        :rtype: dict
        """
        return self._properties['tasks_by_status']

    @property
    def total_tasks(self):
        """
        :returns: The total_tasks
        :rtype: unicode
        """
        return self._properties['total_tasks']

    @property
    def total_workers(self):
        """
        :returns: The total_workers
        :rtype: unicode
        """
        return self._properties['total_workers']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, task_channel=values.unset):
        """
        Fetch a WorkspaceRealTimeStatisticsInstance

        :param unicode task_channel: The task_channel

        :returns: Fetched WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        return self._proxy.fetch(task_channel=task_channel,)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsInstance {}>'.format(context)
