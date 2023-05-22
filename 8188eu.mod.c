#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xce2ebc82, "skb_pull" },
	{ 0x85670f1d, "rtnl_is_locked" },
	{ 0xb8cd532e, "usb_free_coherent" },
	{ 0x2fe252cc, "unregister_inet6addr_notifier" },
	{ 0x449ad0a7, "memcmp" },
	{ 0x999e8297, "vfree" },
	{ 0x952a5d27, "__cfg80211_alloc_event_skb" },
	{ 0xfa8770ac, "wiphy_register" },
	{ 0x57f4a7d2, "nla_put" },
	{ 0xdb89f0cd, "cfg80211_remain_on_channel_expired" },
	{ 0xd6ee688f, "vmalloc" },
	{ 0xa7da5cfa, "nla_put_nohdr" },
	{ 0x8249512, "iwe_stream_add_point" },
	{ 0x5b7307c, "__netdev_alloc_skb" },
	{ 0x66cca4f9, "__x86_indirect_thunk_rcx" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x9d2ab8ac, "__tasklet_schedule" },
	{ 0xc98c4639, "cfg80211_vendor_cmd_reply" },
	{ 0x4cba441d, "iwe_stream_add_event" },
	{ 0xcbd4898c, "fortify_panic" },
	{ 0x2364c85a, "tasklet_init" },
	{ 0x3391256e, "cfg80211_del_sta_sinfo" },
	{ 0xd959cefc, "netif_tx_stop_all_queues" },
	{ 0x81e07163, "seq_release" },
	{ 0xa1b2f0f6, "wiphy_unregister" },
	{ 0x656e4a6e, "snprintf" },
	{ 0xa2e648d5, "usb_autopm_get_interface" },
	{ 0xfb738653, "filp_open" },
	{ 0x37befc70, "jiffies_to_msecs" },
	{ 0x6cf66ff4, "usb_reset_device" },
	{ 0xe2d5255a, "strcmp" },
	{ 0x9e7d6bd0, "__udelay" },
	{ 0xafa1f43b, "usb_alloc_urb" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0x88a0f3de, "__pskb_pull_tail" },
	{ 0xfb578fc5, "memset" },
	{ 0x471a2c4d, "single_open" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xc6f46339, "init_timer_key" },
	{ 0xb45e684d, "napi_schedule_prep" },
	{ 0x7e662233, "param_ops_int" },
	{ 0xe1fcbd4d, "usb_control_msg" },
	{ 0x5b82d1f5, "cfg80211_ch_switch_notify" },
	{ 0xb0e602eb, "memmove" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x9daab73e, "filp_close" },
	{ 0xbea1c7a1, "usb_put_dev" },
	{ 0xd9c18a99, "ieee80211_get_channel_khz" },
	{ 0x5a921311, "strncmp" },
	{ 0x8d5c6c90, "skb_clone" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0xe914e41e, "strcpy" },
	{ 0x117766b, "cfg80211_ready_on_channel" },
	{ 0xe113bbbc, "csum_partial" },
	{ 0x27c7fd3a, "skb_put" },
	{ 0xe8d3ac59, "kernel_read" },
	{ 0xa916b694, "strnlen" },
	{ 0x92c18736, "proc_get_parent_data" },
	{ 0xe6d5209f, "device_set_wakeup_capable" },
	{ 0x6bd0e573, "down_interruptible" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0xf340a9ba, "__netif_napi_del" },
	{ 0x609f1c7e, "synchronize_net" },
	{ 0xd36dc10c, "get_random_u32" },
	{ 0xedf6eef7, "seq_open" },
	{ 0xe46021ca, "_raw_spin_unlock_bh" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0x6383b27c, "__x86_indirect_thunk_rdx" },
	{ 0xa7b4299c, "wiphy_free" },
	{ 0x2f54e997, "param_array_ops" },
	{ 0x94ccce1c, "wiphy_new_nm" },
	{ 0x9cc2caef, "cfg80211_get_bss" },
	{ 0xa6257a2f, "complete" },
	{ 0x6ca0c764, "seq_printf" },
	{ 0x37a0cba, "kfree" },
	{ 0xffbb6ec3, "netif_napi_add_weight" },
	{ 0xc3055d20, "usleep_range_state" },
	{ 0x349cba85, "strchr" },
	{ 0x96b29254, "strncasecmp" },
	{ 0x6bedf402, "ieee80211_freq_khz_to_channel" },
	{ 0x3b82aec4, "__cfg80211_send_event_skb" },
	{ 0x701ef4c6, "init_net" },
	{ 0x9a1dfd65, "strpbrk" },
	{ 0x3e3bad0a, "__tasklet_hi_schedule" },
	{ 0x280f40d4, "kthread_stop" },
	{ 0xb47cca30, "csum_ipv6_magic" },
	{ 0xac9d10cc, "cfg80211_disconnected" },
	{ 0xeb51ecee, "netif_tx_wake_queue" },
	{ 0x1a3ad48f, "cfg80211_michael_mic_failure" },
	{ 0x11407bbd, "device_wakeup_enable" },
	{ 0xeb2aeab0, "skb_dequeue" },
	{ 0x91690dbe, "usb_deregister" },
	{ 0xea3c74e, "tasklet_kill" },
	{ 0xac60c13e, "netif_rx" },
	{ 0x232286b4, "cfg80211_ibss_joined" },
	{ 0x9166fada, "strncpy" },
	{ 0x24d72cd0, "skb_copy_bits" },
	{ 0xc38c83b8, "mod_timer" },
	{ 0x52a79ac6, "param_ops_charp" },
	{ 0x4629334c, "__preempt_count" },
	{ 0x27139d06, "skb_copy" },
	{ 0x5445d134, "seq_lseek" },
	{ 0x996c72f8, "register_netdevice" },
	{ 0xce9f3570, "wake_up_process" },
	{ 0xd69248fe, "kthread_create_on_node" },
	{ 0x55385e2e, "__x86_indirect_thunk_r14" },
	{ 0xa16334bd, "param_ops_uint" },
	{ 0x4971808c, "usb_get_dev" },
	{ 0x2fe81bc5, "netif_carrier_off" },
	{ 0x89940875, "mutex_lock_interruptible" },
	{ 0x4bfec637, "seq_read" },
	{ 0xb55dc13e, "napi_complete_done" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0xcefb0c9f, "__mutex_init" },
	{ 0x4dfa8d4b, "mutex_lock" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0x608741b5, "__init_swait_queue_head" },
	{ 0xd37240ae, "cfg80211_scan_done" },
	{ 0x362f9a8, "__x86_indirect_thunk_r12" },
	{ 0x15ba50a6, "jiffies" },
	{ 0xbd651dae, "remove_proc_entry" },
	{ 0xf68285c0, "register_inetaddr_notifier" },
	{ 0x367b85b8, "cfg80211_roamed" },
	{ 0x9db428ba, "cfg80211_put_bss" },
	{ 0xdcfb8905, "register_netdev" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0x6c6f57fa, "dev_addr_mod" },
	{ 0xfe029963, "unregister_inetaddr_notifier" },
	{ 0xcf2a6966, "up" },
	{ 0xc3690fc, "_raw_spin_lock_bh" },
	{ 0x98794516, "current_task" },
	{ 0x97934ecf, "del_timer_sync" },
	{ 0xeb4f6271, "cfg80211_connect_done" },
	{ 0xee48b5d7, "skb_trim" },
	{ 0xde234379, "kill_pid" },
	{ 0x6df1aaf1, "kernel_sigaction" },
	{ 0xf1969a8e, "__usecs_to_jiffies" },
	{ 0x4a3ad70e, "wait_for_completion_timeout" },
	{ 0x42402f75, "skb_push" },
	{ 0x1000e51, "schedule" },
	{ 0x6008689f, "kthread_complete_and_exit" },
	{ 0x16f86dcf, "usb_alloc_coherent" },
	{ 0x1a412507, "find_vpid" },
	{ 0xe1537255, "__list_del_entry_valid" },
	{ 0xcaa31a8c, "proc_create_data" },
	{ 0xe638abc4, "__dev_kfree_skb_any" },
	{ 0xe8583f58, "cfg80211_unlink_bss" },
	{ 0xeabd8065, "netif_carrier_on" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0x1f3306e, "usb_kill_urb" },
	{ 0x17ee3fe5, "dev_alloc_name" },
	{ 0x92997ed8, "_printk" },
	{ 0x25974000, "wait_for_completion" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0xafd744c6, "__x86_indirect_thunk_rbp" },
	{ 0x2469810f, "__rcu_read_unlock" },
	{ 0x19d3110e, "cfg80211_inform_bss_frame_data" },
	{ 0x9d0d6206, "unregister_netdevice_notifier" },
	{ 0xa2724840, "flush_signals" },
	{ 0xf9a482f9, "msleep" },
	{ 0xf3ccb62d, "unregister_netdev" },
	{ 0x8d522714, "__rcu_read_lock" },
	{ 0x45059f8a, "cfg80211_new_sta" },
	{ 0xb1ab2c5c, "usb_free_urb" },
	{ 0x52514696, "alloc_etherdev_mqs" },
	{ 0x60352082, "register_inet6addr_notifier" },
	{ 0x3213f038, "mutex_unlock" },
	{ 0xc4f0da12, "ktime_get_with_offset" },
	{ 0x760a0f4f, "yield" },
	{ 0xc0b1b21f, "netif_receive_skb" },
	{ 0xb5b54b34, "_raw_spin_unlock" },
	{ 0x5de268d2, "usb_submit_urb" },
	{ 0x68f31cbd, "__list_add_valid" },
	{ 0x62019a6c, "unregister_netdevice_queue" },
	{ 0x15b45af1, "__cfg80211_alloc_reply_skb" },
	{ 0xd58c9d7c, "free_netdev" },
	{ 0x55bec75e, "napi_disable" },
	{ 0x7031f359, "cfg80211_rx_mgmt_ext" },
	{ 0xe0112fc4, "__x86_indirect_thunk_r9" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0xf90a1e85, "__x86_indirect_thunk_r8" },
	{ 0xa225fc36, "wiphy_apply_custom_regulatory" },
	{ 0xda38c0a8, "dev_get_by_name" },
	{ 0x917f35a4, "proc_mkdir_data" },
	{ 0x69acdf38, "memcpy" },
	{ 0x20000329, "simple_strtoul" },
	{ 0xeae3dfd6, "__const_udelay" },
	{ 0x34c8eee3, "skb_queue_tail" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x754d539c, "strlen" },
	{ 0x87237993, "napi_enable" },
	{ 0xd2da1048, "register_netdevice_notifier" },
	{ 0xd0da656b, "__stack_chk_fail" },
	{ 0xf347bb2f, "cfg80211_mgmt_tx_status_ext" },
	{ 0x256938c2, "single_release" },
	{ 0xa22e15, "napi_gro_receive" },
	{ 0x335a3aa7, "eth_type_trans" },
	{ 0x85df9b6c, "strsep" },
	{ 0x892bd6f6, "__napi_schedule" },
	{ 0xb732d645, "usb_register_driver" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0xb83992f2, "module_layout" },
};

MODULE_INFO(depends, "usbcore,cfg80211");

MODULE_ALIAS("usb:v0BDAp8179d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BDAp0179d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v07B8p8179d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BDAp8179d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v2357p010Cd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0DF6p0076d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v2001p330Fd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v2001p3310d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v2001p3311d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v2001p331Bd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v056Ep4008d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v7392pB811d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "E4EFE5255E2F7FAD3716C9A");
