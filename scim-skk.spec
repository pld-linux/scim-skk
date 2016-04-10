Summary:	SCIM IMEngine module for SKK input
Summary(pl.UTF-8):	Silnik IM SCIM dla metody wprowadzania znaków SKK
Name:		scim-skk
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://osdn.jp/projects/scim-imengine/releases/p3205
Source0:	http://dl.osdn.jp/scim-imengine/18121/%{name}-%{version}.tar.gz
# Source0-md5:	69d789660439c248e507da63c90ad70a
Patch0:		%{name}-no-rpath.patch
Patch1:		%{name}-gtk3.patch
URL:		https://osdn.jp/projects/scim-imengine/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.0
Requires:	scim >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM IMEngine module for SKK input.

%description -l pl.UTF-8
Silnik IM SCIM dla metody wprowadzania znaków SKK.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%lang(ja) %doc README.ja
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/skk.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/skk-imengine-setup.so
%{_datadir}/scim/icons/scim-skk.png
