Summary:	A KDE video conversion tool
Summary(pl):	Video konwerter dla KDE
Name:		konverter
Version:	0.93
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.kraus.tk/projects/konverter/sources/%{name}-%{version}.tar.gz
# Source0-md5:	e0dce10b449aaad948f8a749d01e7b00
URL:		http://www.kraus.tk/projects/konverter
BuildRequires:	kdelibs-devel
BuildRequires:	xine-lib-devel
Requires:	mencoder
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konverter is a KDE MEncoder frontend for easy video
conversions,scaling and cropping.

%description -l pl
Konverter jest nak³adk± na MEncoder do ³atwej konwersji video,
skalowania lub wycinania.

%prep
%setup -q -n %{name}

%build
export QTDIR=%{_prefix}
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/kde}

install bin/konverter $RPM_BUILD_ROOT%{_bindir}/konverter
install distfiles/konverter.desktop \
   $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(644,root,root,755)
%doc distfiles/{NEWS,TODO,README,AUTHORS,ChangeLog}
%attr(755,root,root) %{_bindir}/konverter
%{_desktopdir}/kde/%{name}.desktop
