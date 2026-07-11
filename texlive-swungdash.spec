%global tl_name swungdash
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Typeset a swung dash in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/swungdash
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/swungdash.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/swungdash.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The swung dash (U+2053) is a useful character traditionally used in
typesetting dictionaries, but not supported by most typefaces. This
package provides one simple command to typeset a swung dash in XeLaTeX
and LuaLaTeX, by applying transformations to the given font's glyph for
a tilde.

