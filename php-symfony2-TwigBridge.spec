%define		pearname	TwigBridge
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Twig Bridge
Name:		php-symfony2-TwigBridge
Version:	2.4.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	5f06c3267d33c73e6f799dedeb8ff24a
URL:		https://github.com/symfony/TwigBridge
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-twig-Twig >= 1.11
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-HttpKernel
Suggests:	php-symfony2-Routing
Suggests:	php-symfony2-Security
Suggests:	php-symfony2-Templating
Suggests:	php-symfony2-Translation
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides integration for Twig with various Symfony2 components.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Bridge/Twig/Tests .
mv .%{php_pear_dir}/Symfony/Bridge/Twig/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Bridge/Twig/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Bridge/Twig
%{php_pear_dir}/Symfony/Bridge/Twig/*.php
%{php_pear_dir}/Symfony/Bridge/Twig/Extension
%{php_pear_dir}/Symfony/Bridge/Twig/Form
%{php_pear_dir}/Symfony/Bridge/Twig/Node
%{php_pear_dir}/Symfony/Bridge/Twig/NodeVisitor
%{php_pear_dir}/Symfony/Bridge/Twig/Resources
%{php_pear_dir}/Symfony/Bridge/Twig/TokenParser
%{php_pear_dir}/Symfony/Bridge/Twig/Translation
