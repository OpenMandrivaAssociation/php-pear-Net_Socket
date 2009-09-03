%define		_class		Net
%define		_subclass	Socket
%define		_pearname	%{_class}_%{_subclass}

Name:		php-pear-%{_pearname}
Version:	1.0.9
Release:	%mkrel 1
Summary:	Network Socket Interface
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_LDAP2
Source0:	http://download.pear.php.net/package/%{_pearname}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml \
    %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml

