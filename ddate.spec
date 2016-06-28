Name:       ddate   
Version:    0.2.2
Release:    1
Summary:    Convert Gregorian dates to Discordian dates
License:    Public Domain
URL:        https://github.com/bo0ts/%{name}
Source0:    %{url}/archive/v%{version}.tar.gz

BuildRequires:  cmake   

%description
This tool prints a date in the Discordian date format.

%prep
%setup -qn %{name}-%{version}

%build
%cmake
%make

%install
make install DESTDIR=%{buildroot} -C build

%check
ctest

%files
%doc README.org
%{_bindir}/*
%{_mandir}/man1/*
