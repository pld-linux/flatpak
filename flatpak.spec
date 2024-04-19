#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library
%bcond_with	libsoup		# libsoup instead of curl
%bcond_with	selinux		# selinux module for system-helper
%bcond_without	system_bwrap	# system bubblewrap
%bcond_without	malcontent	# parental control support via libmalcontent

Summary:	Application deployment framework for desktop apps
Summary(pl.UTF-8):	Szkielet do wdrażania aplikacji desktopowych
Name:		flatpak
Version:	1.14.6
Release:	1
License:	LGPL v2+
Group:		Applications
#Source0Download: https://github.com/flatpak/flatpak/releases/
Source0:	https://github.com/flatpak/flatpak/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9ac68b1521067c400b3be401e533d20e
URL:		https://flatpak.org/
BuildRequires:	AppStream-devel >= 1.0
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.13.4
BuildRequires:	bison
%{?with_system_bwrap:BuildRequires:	bubblewrap >= 0.5.0}
%{!?with_libsoup:BuildRequires:	curl-devel >= 7.29.0}
BuildRequires:	dconf-devel >= 0.26
%if %{with apidocs}
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl-nons
%endif
# or libelf >= 0.8.12
BuildRequires:	elfutils-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.18.2
BuildRequires:	glib2-devel >= 1:2.60
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	gpgme-devel >= 1:1.8.0
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	libarchive-devel >= 2.8.0
BuildRequires:	libcap-devel
BuildRequires:	libfuse3-devel >= 3.1.1
%{?with_malcontent:BuildRequires:	libmalcontent-devel >= 0.4.0}
BuildRequires:	libseccomp-devel
%{?with_libsoup:BuildRequires:	libsoup-devel >= 2.4}
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.4
%{?with_apidocs:BuildRequires:	libxslt-progs}
BuildRequires:	ostree-devel >= 2020.8
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	polkit-devel >= 0.98
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.720
BuildRequires:	sed >= 4.0
# /usr/share/selinux/devel/Makefile
%{?with_selinux:BuildRequires:	selinux-policy-devel}
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xdg-dbus-proxy >= 0.1.0
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xz
BuildRequires:	zstd-devel >= 0.8.1
# no switch to disable
%{!?with_malcontent:BuildConflicts:	libmalcontent-devel}
%{?with_system_bwrap:Requires:	bubblewrap >= 0.5.0}
Requires:	libfuse3 >= 3.1.1
Requires:	ostree >= 2020.8
Requires:	polkit >= 0.98
Requires:	xdg-dbus-proxy >= 0.1.0
Obsoletes:	xdg-app < 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application deployment framework for desktop apps.

%description -l pl.UTF-8
Szkielet do wdrażania aplikacji desktopowych.

%package libs
Summary:	Shared flatpak library
Summary(pl.UTF-8):	Biblioteka współdzielona flatpak
Group:		Libraries
%{!?with_libsoup:Requires:	curl-libs >= 7.29.0}
Requires:	dconf >= 0.26
Requires:	glib2 >= 1:2.60
Requires:	gpgme >= 1:1.8.0
%{?with_malcontent:Requires:	libmalcontent >= 0.4.0}
Requires:	libxml2 >= 2.4
Requires:	ostree >= 2020.8
Requires:	zstd >= 0.8.1

%description libs
Shared flatpak library.

%description libs -l pl.UTF-8
Biblioteka współdzielona flatpak.

%package devel
Summary:	Header files for flatpak library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki flatpak
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.60
Requires:	ostree-devel >= 2020.8

%description devel
Header files for flatpak library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki flatpak.

%package static
Summary:	Static flatpak library
Summary(pl.UTF-8):	Biblioteka statyczna flatpak
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static flatpak library.

%description static -l pl.UTF-8
Biblioteka statyczna flatpak.

%package apidocs
Summary:	API documentation for flatpak library
Summary(pl.UTF-8):	Dokumentacja API biblioteki flatpak
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for flatpak library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki flatpak.

%package -n bash-completion-flatpak
Summary:	Bash completion for flatpak command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów polecenia flatpak
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2
Obsoletes:	bash-completion-xdg-app < 0.6.0
BuildArch:	noarch

%description -n bash-completion-flatpak
Bash completion for flatpak command.

%description -n bash-completion-flatpak -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia flatpak.

%package -n fish-completion-flatpak
Summary:	Fish completion for flatpak commands
Summary(pl.UTF-8):	Dopełnianie składni poleceń flatpak w fish
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-flatpak
Fish completion for flatpak commands.

%description -n fish-completion-flatpak -l pl.UTF-8
Dopełnianie składni poleceń flatpak w fish.

%package -n zsh-completion-flatpak
Summary:	ZSH completion for flatpak command
Summary(pl.UTF-8):	Uzupełnianie parametrów polecenia flatpak w powłoce ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-flatpak
ZSH completion for flatpak command.

%description -n zsh-completion-flatpak -l pl.UTF-8
Uzupełnianie parametrów polecenia flatpak w powłoce ZSH.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' scripts/flatpak-{bisect,coredumpctl}

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4 -I subprojects/libglnx
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-documentation} \
	%{?with_apidocs:--enable-gtk-doc} \
	--disable-silent-rules \
	%{?with_selinux:--enable-selinux-module} \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir} \
	%{?with_system_bwrap:--with-system-bubblewrap} \
	--with-system-dbus-proxy \
	--with-systemdsystemunitdir=%{systemdunitdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libflatpak.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%doc %{_docdir}/flatpak
%attr(755,root,root) %{_bindir}/flatpak
%attr(755,root,root) %{_bindir}/flatpak-bisect
%attr(755,root,root) %{_bindir}/flatpak-coredumpctl
%if %{without system_bwrap}
%attr(755,root,root) %{_libexecdir}/flatpak-bwrap
%endif
%attr(755,root,root) %{_libexecdir}/flatpak-oci-authenticator
%attr(755,root,root) %{_libexecdir}/flatpak-portal
%attr(755,root,root) %{_libexecdir}/flatpak-session-helper
%attr(755,root,root) %{_libexecdir}/flatpak-system-helper
%attr(755,root,root) %{_libexecdir}/flatpak-validate-icon
%attr(755,root,root) %{_libexecdir}/revokefs-fuse
%attr(755,root,root) /etc/profile.d/flatpak.sh
/etc/dbus-1/system.d/org.freedesktop.Flatpak.SystemHelper.conf
%{_datadir}/dbus-1/services/org.freedesktop.Flatpak.service
%{_datadir}/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
%{_datadir}/dbus-1/services/org.flatpak.Authenticator.Oci.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Flatpak.service
%{_datadir}/polkit-1/actions/org.freedesktop.Flatpak.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.Flatpak.rules
%{systemdunitdir}/flatpak-system-helper.service
%{systemduserunitdir}/flatpak-oci-authenticator.service
%{systemduserunitdir}/flatpak-portal.service
%{systemduserunitdir}/flatpak-session-helper.service
%attr(755,root,root) %{_prefix}/lib/systemd/system-environment-generators/60-flatpak-system-only
%attr(755,root,root) %{_prefix}/lib/systemd/user-environment-generators/60-flatpak
%{_prefix}/lib/sysusers.d/flatpak.conf
%{systemdtmpfilesdir}/flatpak.conf
%dir %{_datadir}/flatpak
%dir %{_datadir}/flatpak/triggers
%attr(755,root,root) %{_datadir}/flatpak/triggers/*.trigger
%{_mandir}/man1/flatpak*.1*
%{_mandir}/man5/flatpak-flatpakref.5*
%{_mandir}/man5/flatpak-flatpakrepo.5*
%{_mandir}/man5/flatpak-installation.5*
%{_mandir}/man5/flatpak-metadata.5*
%{_mandir}/man5/flatpak-remote.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflatpak.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflatpak.so.0
%{_libdir}/girepository-1.0/Flatpak-1.0.typelib
%{_datadir}/dbus-1/interfaces/org.freedesktop.Flatpak.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Flatpak.Authenticator.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflatpak.so
%{_includedir}/flatpak
%{_datadir}/gir-1.0/Flatpak-1.0.gir
%{_pkgconfigdir}/flatpak.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libflatpak.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/flatpak
%endif

%files -n bash-completion-flatpak
%defattr(644,root,root,755)
%{bash_compdir}/flatpak

%files -n fish-completion-flatpak
%defattr(644,root,root,755)
%{fish_compdir}
%{_datadir}/fish/vendor_conf.d/flatpak.fish

%files -n zsh-completion-flatpak
%defattr(644,root,root,755)
%{zsh_compdir}/_flatpak
