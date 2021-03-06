# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time
from openerp.report import report_sxw


class analytic_wip_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(analytic_wip_report, self).__init__(
            cr, uid, name, context=context
        )
        self.localcontext.update({
            'time': time,
        })

report_sxw.report_sxw(
    'report.analytic.wip',
    'account.analytic.account',
    'addons/analytic_wip_report/report/analytic_wip_report.rml',
    parser=analytic_wip_report, header="internal landscape"
)
