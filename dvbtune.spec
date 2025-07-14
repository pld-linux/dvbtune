Summary:	Tuning application for DVB cards
Summary(pl.UTF-8):	Aplikacja do strojenia kart DVB
Name:		dvbtune
Version:	0.5
Release:	5
License:	GPL v2+
Group:		Networking
Source0:	http://downloads.sourceforge.net/dvbtools/%{name}-%{version}.tar.gz
# Source0-md5:	5212564c786f2538db753214e0e21473
Patch0:		%{name}-dumb31adapters.patch
Patch1:		define-int-types.patch
Patch2:		%{name}-dvr.patch
Patch3:		%{name}-frequency.patch
URL:		http://dvbtools.sourceforge.net/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple tuning application for DVB cards.

%description -l pl.UTF-8
Prosta aplikacja do strojenia kart DVB.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p0

%build
%{__make} %{name} xml2vdr \
	CFLAGS="%{rpmcflags} -I%{_includedir}/libxml2 -DNEWSTRUCT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} xml2vdr $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc scripts README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/xml2vdr
