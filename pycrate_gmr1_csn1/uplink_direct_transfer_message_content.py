# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_gmr1_csn1/uplink_direct_transfer_message_content.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-13
# section: 9.2.56          UPLINK DIRECT TRANSFER
# top-level object: UPLINK DIRECT TRANSFER message content

# external references
from pycrate_gmr1_csn1.nas_message_ie import nas_message_ie
from pycrate_gmr1_csn1.cn_domain_identity_ie import cn_domain_identity_ie
from pycrate_gmr1_csn1.integrity_check_info_ie import integrity_check_info_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

uplink_direct_transfer_message_content = CSN1List(name='uplink_direct_transfer_message_content', list=[
  CSN1Ref(name='cn_domain_identity', obj=cn_domain_identity_ie),
  CSN1Ref(name='nas_message', obj=nas_message_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='integrity_check_info', obj=integrity_check_info_ie)])})])

