# -*- coding: utf-8 -*-
# author: huashaw
from __future__ import absolute_import
from celery import shared_task,task
import datetime
from apps.contract.models import Contract, ContractExpire
from . import models

@shared_task()
def contract_expiration_reminder_30day():
    contract_expiration_reminder(30)
    pass


def contract_expiration_reminder(days):
    qs_contract = Contract.objects.all().filter(datetime.datetime.now().date()
                                                - Contract.contract_end_date <= days)
    qs_contract_expire = ContractExpire.objects.all().delete()

    for contract in qs_contract:
        qs_contract_expire = models.ContractExpire()
        qs_contract_expire.contract_expire_number = contract.contract_number
        qs_contract_expire.contract_expire_name = contract.contract_name
        qs_contract_expire.contract_expire_end_date = contract.contract_end_date
        qs_contract_expire.save()


