Summary:    A gif desktop recorder 
Name:       byzanz
Version:    0.2.3
Release:    %mkrel 2
URL:        https://www.freedesktop.org/~company/
License:    LGPLv3+
Source0:    http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Group:      Video
BuildRequires: gnome-panel-devel
BuildRequires: libxdamage-devel
BuildRequires: cairo-devel >= 1.9.1
BuildRequires: gtk+2-devel >= 2.17.10
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libGConf2-devel
BuildRequires: intltool
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description 
Byzanz is a desktop recorder. Just like Istanbul. But it doesn't record to 
Ogg Theora, but to GIF.

%prep
%setup -q 

%build
%configure2_5x
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

%define schemas %name
%post
%post_install_gconf_schemas %{schemas}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %{schemas}

%postun
%clean_icon_cache hicolor

%clean
rm -Rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog README NEWS AUTHORS 
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/*
%_libdir/%{name}-applet
%_libdir/bonobo/servers/*
%_datadir/gnome-2.0/ui/*
%_datadir/icons/hicolor/*/apps/*
%_mandir/man1/*

