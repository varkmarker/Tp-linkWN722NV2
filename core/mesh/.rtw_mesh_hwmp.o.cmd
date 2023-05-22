cmd_/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o :=  gcc-12 -Wp,-MMD,/home/varkmarker/Tp-linkWN722NV2/core/mesh/.rtw_mesh_hwmp.o.d -nostdinc -I/usr/src/linux-headers-6.1.0-kali9-common/arch/x86/include -I./arch/x86/include/generated -I/usr/src/linux-headers-6.1.0-kali9-common/include -I./include -I/usr/src/linux-headers-6.1.0-kali9-common/arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I/usr/src/linux-headers-6.1.0-kali9-common/include/uapi -I./include/generated/uapi -include /usr/src/linux-headers-6.1.0-kali9-common/include/linux/compiler-version.h -include /usr/src/linux-headers-6.1.0-kali9-common/include/linux/kconfig.h -include /usr/src/linux-headers-6.1.0-kali9-common/include/linux/compiler_types.h -D__KERNEL__ -fmacro-prefix-map=/usr/src/linux-headers-6.1.0-kali9-common/= -Wall -Wundef -Werror=strict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Wno-format-security -std=gnu11 -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -mindirect-branch-cs-prefix -mfunction-return=thunk-extern -fno-jump-tables -mharden-sls=all -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-address-of-packed-member -O2 -fno-allow-store-data-races -Wframe-larger-than=2048 -fstack-protector-strong -Wno-main -Wno-unused-but-set-variable -Wno-unused-const-variable -Wno-dangling-pointer -ftrivial-auto-var-init=zero -fno-stack-clash-protection -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -Wdeclaration-after-statement -Wvla -Wno-pointer-sign -Wcast-function-type -Wno-stringop-truncation -Wno-stringop-overflow -Wno-restrict -Wno-maybe-uninitialized -Wno-array-bounds -Wno-alloc-size-larger-than -Wimplicit-fallthrough=5 -fno-strict-overflow -fno-stack-check -fconserve-stack -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -Wno-packed-not-aligned -g -fno-pie -O1 -Wno-unused-variable -Wno-unused-value -Wno-unused-label -Wno-unused-parameter -Wno-unused-function -Wno-unused -Wno-address -Wno-cast-function-type -Wno-uninitialized -Wno-sometimes-uninitialized -Wno-enum-conversion -Wno-vla -Wno-date-time -Wno-date-time -I/home/varkmarker/Tp-linkWN722NV2/include -I/usr/src/linux-headers-6.1.0-kali9-common//home/varkmarker/Tp-linkWN722NV2/include -I/home/varkmarker/Tp-linkWN722NV2/platform -I/usr/src/linux-headers-6.1.0-kali9-common//home/varkmarker/Tp-linkWN722NV2/platform -I/home/varkmarker/Tp-linkWN722NV2/hal/btc -I/usr/src/linux-headers-6.1.0-kali9-common//home/varkmarker/Tp-linkWN722NV2/hal/btc -I/home/varkmarker/Tp-linkWN722NV2/hal/phydm -I/usr/src/linux-headers-6.1.0-kali9-common//home/varkmarker/Tp-linkWN722NV2/hal/phydm -DCONFIG_RTL8188E -DCONFIG_MP_INCLUDED -DCONFIG_EFUSE_CONFIG_FILE -DEFUSE_MAP_PATH=\"/system/etc/wifi/wifi_efuse_8188eu.map\" -DWIFIMAC_PATH=\"/data/wifimac.txt\" -DCONFIG_LOAD_PHY_PARA_FROM_FILE -DREALTEK_CONFIG_PATH=\"/lib/firmware/\" -DCONFIG_TXPWR_BY_RATE_EN=0 -DCONFIG_TXPWR_LIMIT_EN=0 -DCONFIG_RTW_ADAPTIVITY_EN=0 -DCONFIG_RTW_ADAPTIVITY_MODE=0 -DCONFIG_BR_EXT '-DCONFIG_BR_EXT_BRNAME="'br0'"' -DCONFIG_WIFI_MONITOR -DCONFIG_RTW_NAPI -DCONFIG_RTW_GRO -DCONFIG_RTW_NETIF_SG -DCONFIG_RTW_WIFI_HAL -DCONFIG_RTW_CFGVEDNOR_LLSTATS -DDM_ODM_SUPPORT_TYPE=0x04 -DCONFIG_LITTLE_ENDIAN -DCONFIG_IOCTL_CFG80211 -DRTW_USE_CFG80211_STA_EVENT -I/home/varkmarker/Tp-linkWN722NV2/hal/phydm  -DMODULE  -DKBUILD_BASENAME='"rtw_mesh_hwmp"' -DKBUILD_MODNAME='"8188eu"' -D__KBUILD_MODNAME=kmod_8188eu -c -o /home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o /home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.c   ; ./tools/objtool/objtool --hacks=jump_label --hacks=noinstr --orc --retpoline --rethunk --sls --static-call --uaccess   --module /home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o

source_/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o := /home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.c

deps_/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o := \
    $(wildcard include/config/RTW_MESH) \
    $(wildcard include/config/RTW_MESH_ON_DMD_GANN) \
    $(wildcard include/config/RTW_MESH_ADD_ROOT_CHK) \
  /usr/src/linux-headers-6.1.0-kali9-common/include/linux/compiler-version.h \
    $(wildcard include/config/CC_VERSION_TEXT) \
  /usr/src/linux-headers-6.1.0-kali9-common/include/linux/kconfig.h \
    $(wildcard include/config/CPU_BIG_ENDIAN) \
    $(wildcard include/config/BOOGER) \
    $(wildcard include/config/FOO) \
  /usr/src/linux-headers-6.1.0-kali9-common/include/linux/compiler_types.h \
    $(wildcard include/config/DEBUG_INFO_BTF) \
    $(wildcard include/config/PAHOLE_HAS_BTF_TAG) \
    $(wildcard include/config/HAVE_ARCH_COMPILER_H) \
    $(wildcard include/config/CC_HAS_ASM_INLINE) \
  /usr/src/linux-headers-6.1.0-kali9-common/include/linux/compiler_attributes.h \
  /usr/src/linux-headers-6.1.0-kali9-common/include/linux/compiler-gcc.h \
    $(wildcard include/config/RETPOLINE) \
    $(wildcard include/config/ARCH_USE_BUILTIN_BSWAP) \
    $(wildcard include/config/SHADOW_CALL_STACK) \
    $(wildcard include/config/KCOV) \

/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o: $(deps_/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o)

$(deps_/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o):

/home/varkmarker/Tp-linkWN722NV2/core/mesh/rtw_mesh_hwmp.o: $(wildcard ./tools/objtool/objtool)
