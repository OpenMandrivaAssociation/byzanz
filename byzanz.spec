Summary:    A gif desktop recorder 
Name:       byzanz
Version:    0.1.1
Release:    %mkrel 6
URL:        http://www.freedesktop.org/~company/
License:    GPL
Source0:    http://www.freedesktop.org/~company/%{name}/%{name}-%{version}.tar.bz2
Group:      Video
BuildRequires: libgnomeui2-devel gnome-panel-devel
BuildRequires: libxdamage-devel
BuildRequires: perl-XML-Parser
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description 
Byzanz is a desktop recorder. Just like Istanbul. But it doesn't record to 
Ogg Theora, but to GIF.

%prep
%setup -q 

%build
%configure
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

