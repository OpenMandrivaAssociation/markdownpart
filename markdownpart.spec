%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Markdown display engine for Plasma
Name:		markdownpart
Version:	21.08.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake
BuildRequires:	ninja

%description
Markdown display engine for Plasma

%files -f %{name}.lang
%{_libdir}/qt5/plugins/kf5/parts/markdownpart.so
%{_datadir}/kservices5/markdownpart.desktop
%{_datadir}/metainfo/org.kde.markdownpart.metainfo.xml

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html
