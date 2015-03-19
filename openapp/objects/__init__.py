#    Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# NOTE(comstud): You may scratch your head as you see code that imports
# this module and then accesses attributes for objects such as Instance,
# etc, yet you do not see these attributes in here. Never fear, there is
# a little bit of magic. When objects are registered, an attribute is set
# on this module automatically, pointing to the newest/latest version of
# the object.


def register_all():
    # NOTE(danms): You must make sure your object gets imported in this
    # function in order for it to be registered by services that may
    # need to receive it via RPC.
    pass
    #__import__('openapp.objects.agent')
    #__import__('openapp.objects.aggregate')
    #__import__('openapp.objects.bandwidth_usage')
    #__import__('openapp.objects.block_device')
    #__import__('openapp.objects.compute_node')
    #__import__('openapp.objects.dns_domain')
    #__import__('openapp.objects.ec2')
    #__import__('openapp.objects.external_event')
    #__import__('openapp.objects.fixed_ip')
    #__import__('openapp.objects.flavor')
    #__import__('openapp.objects.floating_ip')
    #__import__('openapp.objects.hv_spec')
    #__import__('openapp.objects.instance')
    #__import__('openapp.objects.instance_action')
    #__import__('openapp.objects.instance_fault')
    #__import__('openapp.objects.instance_group')
    #__import__('openapp.objects.instance_info_cache')
    #__import__('openapp.objects.instance_numa_topology')
    #__import__('openapp.objects.instance_pci_requests')
    #__import__('openapp.objects.keypair')
    #__import__('openapp.objects.migration')
    #__import__('openapp.objects.network')
    #__import__('openapp.objects.network_request')
    #__import__('openapp.objects.numa')
    #__import__('openapp.objects.pci_device')
    #__import__('openapp.objects.pci_device_pool')
    #__import__('openapp.objects.tag')
    #__import__('openapp.objects.quotas')
    #__import__('openapp.objects.security_group')
    #__import__('openapp.objects.security_group_rule')
    #__import__('openapp.objects.service')
    #__import__('openapp.objects.vcpu_model')
    #__import__('openapp.objects.virt_cpu_topology')
    #__import__('openapp.objects.virtual_interface')
