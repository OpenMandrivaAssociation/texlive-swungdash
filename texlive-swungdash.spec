Name:		texlive-swungdash
Version:	64204
Release:	2
Summary:	Typeset a swung dash in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/swungdash
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swungdash.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swungdash.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The swung dash (U+2053) is a useful character traditionally
used in typsetting dictionaries, but not supported by most
typefaces. This package provides one simple command to typeset
a swung dash in XeLaTeX and LuaLaTeX, by applying
transformations to the given font's glyph for a tilde.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/swungdash
%doc %{_texmfdistdir}/doc/latex/swungdash

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
