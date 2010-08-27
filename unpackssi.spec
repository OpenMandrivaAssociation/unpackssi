%define name	unpackssi
%define version	20030612
%define release	%mkrel 1

Name:		%{name}
Summary:	.SSI File Unpacker
Version:	%{version}
Release:	%{release}
Source0:	http://static.jonof.id.au/dl/%{name}.zip
Patch0:		unpackssi-20030612-mdv-linuxify.patch
URL:		http://www.jonof.id.au/misc#unpackssi

Group:		Archiving/Compression
BuildRoot:	%{_tmppath}/%{name}-%{version}
License:	GPLv2

%description
This is a small program to extract the files from the .SSI package format
which Sunstorm Interactive expansion packs for games like Duke Nukem 3D
are distributed in.


%prep
%setup -q -c
%patch0 -p1

%build
%make CFLAGS="%{optflags} %{ldflags}"

%install
rm -rf %{buildroot}
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt
%{_bindir}/%{name}
