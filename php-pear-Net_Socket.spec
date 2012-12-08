%define		_class		Net
%define		_subclass	Socket
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.10
Release:	%mkrel 4
Summary:	Network Socket Interface
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_LDAP2
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2mdv2011.0
+ Revision: 667634
- mass rebuild

* Mon Oct 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-1mdv2011.0
+ Revision: 586624
- update to new version 1.0.10

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-4mdv2010.1
+ Revision: 468722
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Nov 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-3mdv2010.1
+ Revision: 463808
- use rpm filetriggers to register starting from mandriva 2010.1

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-2mdv2010.0
+ Revision: 449347
- use pear installer
- use fedora %%post/%%postun

* Thu Sep 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-1mdv2010.0
+ Revision: 428988
- import php-pear-Net_Socket


* Thu Sep 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-1mdv2010.0
- first mdv release
