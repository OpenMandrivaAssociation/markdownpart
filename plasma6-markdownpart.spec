#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Markdown display engine for Plasma
Name:		plasma6-markdownpart
Version:	24.08.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/markdownpart/-/archive/%{gitbranch}/markdownpart-%{gitbranchd}.tar.bz2#/markdownpart-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/markdownpart-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake
BuildRequires:	ninja

%description
Markdown display engine for Plasma

%files -f markdownpart.lang
%{_libdir}/qt6/plugins/kf6/parts/markdownpart.so
%{_datadir}/metainfo/org.kde.markdownpart.metainfo.xml

%prep
%autosetup -p1 -n markdownpart-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang markdownpart --with-html
