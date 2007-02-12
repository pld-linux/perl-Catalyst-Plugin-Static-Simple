#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Static-Simple
Summary:	Catalyst::Plugin::Static::Simple - make serving static pages painless
Summary(pl.UTF-8):   Catalyst::Plugin::Static::Simple - bezpolesne serwowanie stron statycznych
Name:		perl-Catalyst-Plugin-Static-Simple
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d852a4835ed664af1d7a82b62f0a72cd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.30
BuildRequires:	perl-MIME-Types >= 1.15
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Static::Simple plugin is designed to make serving static content
in your application during development quick and easy, without
requiring a single line of code from you.

It will detect static files used in your application by looking for
file extensions in the URI. By default, you can simply load this
plugin and it will immediately begin serving your static files with
the correct MIME type. The light-weight MIME::Types module is used to
map file extensions to IANA-registered MIME types.

%description -l pl.UTF-8
Wtyczka Static::Simple została zaprojektowana aby uczynić serwowanie
statycznej treści z aplikacji w czasie tworzenia szybkim i łatwym, nie
wymagającym napisania ani jednej linii kodu.

Wtyczka ta wykrywa statyczne pliki użyte w aplikacji szukając
rozszerzeń pliku w URI. Domyślnie można po prostu wczytać tę wtyczkę,
a ona natychmiast zacznie serwować statyczne pliki z poprawnym typem
MIME. Do odwzorowywania rozszerzeń plików na typy MIME zarejestrowane
w IANA został wykorzystany lekki moduł MIME::Types.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Catalyst/Plugin/Static
%{perl_vendorlib}/Catalyst/Plugin/Static/*.pm
%{_mandir}/man3/*
