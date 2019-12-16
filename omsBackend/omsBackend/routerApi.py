# -*- coding: utf-8 -*-
# author: huashaw

from rest_framework.routers import DefaultRouter
from apps.records.views import RecordViewSet
from apps.users.views import UserViewSet, RoleViewSet, GroupViewSet
from apps.worktickets.views import WorkTicketViewSet, TicketCommentViewSet, TicketEnclosureViewSet, TicketTypeViewSet
from apps.tools.views import UploadViewSet, SendmailViewSet, SendmessageViewSet, CalenderViewSet, FileUploadViewSet
from apps.menus.views import FirstmenuViewSet, SecondmenuViewSet, ElementViewSet
from apps.perms.views import UserMenuPermsViewSet, UserHostPermsViewSet, UserWikiPermsViewSet
from apps.wikis.views import WikiViewSet
from apps.hosts.views import HostViewSet, IdcViewSet, HostGroupViewSet
from apps.jobs.views import JobsViewSet, DeployenvViewSet, DeploycmdViewSet, DeployJobsViewSet, DeployTicketViewSet, \
    DeployTicketEnclosureViewSet, SqlTicketTicketViewSet, DeployResultsViewSet

from apps.salts.views import SaltStateViewSet, StateJobViewSet, SaltStateGroupViewSet, SaltServerViewSet
from apps.computer_room.views import ComputerRoomViewSet
from apps.managelink.views import ManageLinkViewSet
from apps.CabinetType.views import CabinetViewSet
from apps.NetworkDev.views import NetdevViewSet
from apps.Parts.views import PartsViewSet
from apps.servers.views import ServersViewSet, VMServersViewSet
from apps.process.views import ProcessViewSet, IPPortBindingViewSets
from apps.IPResource.views import IPResourceViewSet



router = DefaultRouter()


router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)


router.register(r'worktickers', WorkTicketViewSet)
router.register(r'ticketcomments', TicketCommentViewSet)
router.register(r'ticketenclosures', TicketEnclosureViewSet)
router.register(r'tickettypes', TicketTypeViewSet)


router.register(r'upload', UploadViewSet)
router.register(r'sendmail', SendmailViewSet)
router.register(r'sendmessage', SendmessageViewSet)
router.register(r'calenders', CalenderViewSet)
router.register(r'fileupload', FileUploadViewSet)


router.register(r'firstmenus', FirstmenuViewSet)
router.register(r'secondmenus', SecondmenuViewSet)
router.register(r'menumetas', ElementViewSet)


router.register(r'usermenuperms', UserMenuPermsViewSet)
router.register(r'userhostperms', UserHostPermsViewSet)
router.register(r'userwikiperms', UserWikiPermsViewSet)


router.register(r'wikis', WikiViewSet)


router.register(r'hosts', HostViewSet)
router.register(r'idcs', IdcViewSet)
router.register(r'hostgroups', HostGroupViewSet)


router.register(r'jobs', JobsViewSet)
router.register(r'deployenvs', DeployenvViewSet)
router.register(r'deploycmds', DeploycmdViewSet)
router.register(r'deployjobs', DeployJobsViewSet)
router.register(r'deployresults', DeployResultsViewSet)
router.register(r'deploytickets', DeployTicketViewSet)
router.register(r'deployticketenclosures', DeployTicketEnclosureViewSet)
router.register(r'sqltickets', SqlTicketTicketViewSet)

router.register(r'records', RecordViewSet)

router.register(r'saltstates', SaltStateViewSet)
router.register(r'saltstategroups', SaltStateGroupViewSet)
router.register(r'saltjobs', StateJobViewSet)
router.register(r'saltservers', SaltServerViewSet)
router.register(r'computerroom', ComputerRoomViewSet)
router.register(r'managelink', ManageLinkViewSet)
router.register(r'cabinet', CabinetViewSet)
router.register(r'netdev', NetdevViewSet)
router.register(r'parts', PartsViewSet)
router.register(r'servers', ServersViewSet)
router.register(r'vmservers', VMServersViewSet)
router.register(r'process', ProcessViewSet)
router.register(r'IPPortBinding', IPPortBindingViewSets)
router.register(r'IPResource', IPResourceViewSet)

# from projects.views import ProjectViewSet, ProjectCommentViewSet, ProjectEnclosureViewSet, ProjectTypeViewSet, \
#     BugManagerViewSet, TestManagerViewSet, DemandManagerViewSet, DemandEnclosureViewSet, ProjectCompleteViewSet
#
# router.register(r'projects', ProjectViewSet)
# router.register(r'projectcompletes', ProjectCompleteViewSet)
# router.register(r'projectcomments', ProjectCommentViewSet)
# router.register(r'projectenclosures', ProjectEnclosureViewSet)
# router.register(r'projecttypes', ProjectTypeViewSet)
# router.register(r'bugmanagers', BugManagerViewSet)
# router.register(r'testmanagers', TestManagerViewSet)
# router.register(r'demandmanagers', DemandManagerViewSet)
# router.register(r'demandenclosures', DemandEnclosureViewSet)
#
# from optasks.views import OpsProjectViewSet, OpsDemandManagerViewSet, ProjectCommentViewSet
#
# router.register(r'opsprojects', OpsProjectViewSet)
# router.register(r'opsdemandmanagers', OpsDemandManagerViewSet)
# router.register(r'opsprojectcomments', ProjectCommentViewSet)

# from dnsmanager.views import DnsApiKeyViewSet, DnsDomainViewSet, DnsRecordViewSet, DnspodDomainViewSet, \
#     DnspodRecordViewSet, GodaddyDomainViewSet, GodaddyRecordViewSet, BindDomainViewSet, BindRecordViewSet
#
# router.register(r'dnsapikeys', DnsApiKeyViewSet)
# router.register(r'dnsdomains', DnsDomainViewSet)
# router.register(r'dnsrecords', DnsRecordViewSet)
# router.register(r'dnspoddomains', DnspodDomainViewSet, base_name='dnspoddomains')
# router.register(r'dnspodrecords', DnspodRecordViewSet, base_name='dnspodrecords')
# router.register(r'godaddydomains', GodaddyDomainViewSet, base_name='godaddydomains')
# router.register(r'godaddyreecords', GodaddyRecordViewSet, base_name='godaddyreecords')
# router.register(r'binddomains', BindDomainViewSet, base_name='binddomains')
# router.register(r'bindrecords', BindRecordViewSet, base_name='bindrecords')
#
# from zkmanager.views import ZkUserViewSet, PunchViewSet, PunchSetViewSet
#
# router.register(r'zkusers', ZkUserViewSet)
# router.register(r'zkpunchs', PunchViewSet)
# router.register(r'zkpunchset', PunchSetViewSet)

# from zbmanager.views import ZbHostViewSet, ZbHostGroupViewSet, ZbTemplateViewSet
#
# router.register(r'zbhosts', ZbHostViewSet, base_name='zbhosts')
# router.register(r'zbhostgroups', ZbHostGroupViewSet, base_name='zbhostgroups')
# router.register(r'zbtemplates', ZbTemplateViewSet, base_name='zbtemplates')
