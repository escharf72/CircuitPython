<!DOCTYPE html>
<!-- saved from url=(0042)https://github.com/escharf72/CircuitPython -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-lEwNhIgWxFtdGboTlCciWWGiX2vG3LOojEE671oRJEhnPj6jpmgQTJtpq3O2KBzCcln6RzwfvHlyFaI/oR+RNQ==" rel="stylesheet" href="./hello_vs_code_files/frameworks-849637ecbd4bd65815cc113d80fee2d4.css">
  
    <link crossorigin="anonymous" media="all" integrity="sha512-nbXfO4fh1nahyjggjTnpWxGoA7FoTdx2f21d62JQeVn0RlLoYci8FX3fuqk4Sn/kD8Yuzgd/IHXroBMoxFLFWA==" rel="stylesheet" href="./hello_vs_code_files/github-8fec968b4bdafcef25940c968feaf09b.css">
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>escharf72/CircuitPython</title>
    <meta name="description" content="Contribute to escharf72/CircuitPython development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars1.githubusercontent.com/u/54952359?s=400&amp;v=4"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="escharf72/CircuitPython"><meta name="twitter:description" content="Contribute to escharf72/CircuitPython development by creating an account on GitHub.">
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/54952359?s=400&amp;v=4"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="escharf72/CircuitPython"><meta property="og:url" content="https://github.com/escharf72/CircuitPython"><meta property="og:description" content="Contribute to escharf72/CircuitPython development by creating an account on GitHub.">

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NDQ5NTk3MzAwOjAwOTI4ZjllNGI2NGNkNTM2M2M2NjlkZGNlOTZmODg2MjBjYmQyYzdiZDkyOGJkMGQyMGFjYjRiODQ5ZTExZGI=--1dd56a2ad4a71f5c9e6d97d0e4c627418e3bdce1">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="https://github.com/sessions/sudo_modal">
  <meta name="request-id" content="E9D4:07B5:50D56D:7E91E7:5D8E31B9" data-pjax-transient="">


  

  <meta name="selected-link" value="repo_source" data-pjax-transient="">

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com"><meta name="octolytics-app-id" content="github"><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event"><meta name="octolytics-dimension-request_id" content="E9D4:07B5:50D56D:7E91E7:5D8E31B9"><meta name="octolytics-dimension-region_edge" content="iad"><meta name="octolytics-dimension-region_render" content="iad"><meta name="octolytics-dimension-ga_id" content="319224609.1566489106" class="js-octo-ga-id"><meta name="octolytics-dimension-visitor_id" content="8435015651480746513"><meta name="octolytics-actor-id" content="54952359"><meta name="octolytics-actor-login" content="escharf72"><meta name="octolytics-actor-hash" content="df2a1ce9d5663e0f35c66cb5d3bb676944a5eb5258667e55b13a66f2078f269f">
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-pjax-transient="true">



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="fb4ef62e33630f1082ee70cc0fa45868">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="escharf72">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YTVjZTdjYzViZmVjNzU3MTcwOWFhYzBiZDU4ZWE1YmM3ZmJmYzg5NmVhMjdhN2E1YTQ2MTdjODcyYjJlYjlhMnx7InJlbW90ZV9hZGRyZXNzIjoiNjcuMTMyLjQ5LjE4IiwicmVxdWVzdF9pZCI6IkU5RDQ6MDdCNTo1MEQ1NkQ6N0U5MUU3OjVEOEUzMUI5IiwidGltZXN0YW1wIjoxNTY5NTk5OTMyLCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="ACTIONS_V2_ON_MARKETPLACE,MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS,NOTIFY_ON_BLOCK,RELATED_ISSUES,GHE_CLOUD_TRIAL">

  <meta name="html-safe-nonce" content="787859a37f768d20a71bf5eddfe75980310f41a1">

  <meta http-equiv="x-pjax-version" content="708e5fb3eaa33220d9dc529021f1916b">
  

      <link href="https://github.com/escharf72/CircuitPython/commits/master.atom" rel="alternate" title="Recent Commits to CircuitPython:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/escharf72/CircuitPython git https://github.com/escharf72/CircuitPython.git">

  <meta name="octolytics-dimension-user_id" content="54952359"><meta name="octolytics-dimension-user_login" content="escharf72"><meta name="octolytics-dimension-repository_id" content="206609099"><meta name="octolytics-dimension-repository_nwo" content="escharf72/CircuitPython"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="206609099"><meta name="octolytics-dimension-repository_network_root_nwo" content="escharf72/CircuitPython"><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false">


    <link rel="canonical" href="https://github.com/escharf72/CircuitPython" data-pjax-transient="">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <meta name="webauthn-auth-enabled" content="true">

  <meta name="webauthn-registration-enabled" content="true">

  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

  </head>

  <body class="logged-in env-production min-width-lg">
    

  <div class="position-relative js-header-wrapper ">
    <a href="https://github.com/escharf72/CircuitPython#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


          <header class="Header" role="banner">

    <div class="Header-item">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>

    </div>


    <div class="Header-item Header-item--full">
        <div class="header-search mr-3 scoped-search site-scoped-search js-site-search position-relative js-jump-to" role="combobox" aria-owns="jump-to-results" aria-label="Search or jump to" aria-haspopup="listbox" aria-expanded="false">
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="206609099" data-scoped-search-url="/escharf72/CircuitPython/search" data-unscoped-search-url="/search" action="https://github.com/escharf72/CircuitPython/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="✓">
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" name="q" value="" placeholder="Search or jump to…" data-unscoped-placeholder="Search or jump to…" data-scoped-placeholder="Search or jump to…" autocapitalize="off" aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search or jump to…" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=iwURdYH7peqnJPPZ5S46ii4a7KyoktEjLn+eScaUbIph1gYMFBNRtsbO8henlJAz4712wjHs/q8oIyyAmvbGzg==" spellcheck="false" autocomplete="off">
          <input type="hidden" class="js-site-search-type-field" name="type">
            <img src="./hello_vs_code_files/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/escharf72/CircuitPython">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/escharf72/CircuitPython" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/escharf72/CircuitPython">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/escharf72/CircuitPython" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/escharf72/CircuitPython">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/escharf72/CircuitPython" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="./hello_vs_code_files/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


      <nav class="d-flex" aria-label="Global">

  <a class="js-selected-navigation-item Header-link  mr-3" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="https://github.com/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link  mr-3" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="https://github.com/issues">
    Issues
</a>
    <div class="mr-3">
      <a class="js-selected-navigation-item Header-link" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="https://github.com/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link  mr-3" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="https://github.com/explore">
    Explore
</a>

</nav>

    </div>



    <div class="Header-item">
      

    <a aria-label="You have no unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-s js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:54952359" href="https://github.com/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"></path></svg>
</a>
    </div>


    <div class="Header-item position-relative">
      <details class="details-overlay details-reset">
  <summary class="Header-link" aria-label="Create new…" data-ga-click="Header, create new, icon:add" aria-haspopup="menu" role="button">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"></path></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw" role="menu">
    
<a role="menuitem" class="dropdown-item" href="https://github.com/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="https://github.com/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="https://github.com/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="escharf72/CircuitPython">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="https://github.com/escharf72/CircuitPython/issues/new" data-ga-click="Header, create new issue" data-skip-pjax="">
      New issue
    </a>


  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0">
      
<details class="details-overlay details-reset">
  <summary class="Header-link" aria-label="View profile and more" data-ga-click="Header, show menu, icon:avatar" aria-haspopup="menu" role="button">
    <img alt="@escharf72" class="avatar" src="./hello_vs_code_files/54952359" height="20" width="20">
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-2" style="width: 180px" role="menu">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="https://github.com/escharf72" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">escharf72</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled="">
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit " role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:54952359,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:54952359,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;}}" data-hydro-click-hmac="95a52fbed0fc3312d620a95b00b216549ca854820f6a19401057f990e02d5e63">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
" style="max-width: 29px">
          <div class="user-status-emoji-container flex-shrink-0 mr-1 mt-1 lh-condensed-ultra v-align-bottom" style="">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 0 1-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 0 1-1.45-2.17A6.59 6.59 0 0 1 1.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 0 1 8 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"></path></svg>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6" style="line-height: 20px;">
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
              <span class="text-gray ml-2">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1" aria-modal="true">
      <!-- '"` --><!-- </textarea></xmp> --><form class="position-relative flex-auto js-user-status-form" action="https://github.com/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="_method" value="put"><input type="hidden" name="authenticity_token" value="PW/XHLkjUnFoGISBrBT8MLa/4rnYhkLnsxRgI6O37iwNM43r+9nx6rUwJfDNL7nnwwUZBMjg7eLcX4kYP7jTMQ==">
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog="">
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden=""></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon">
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 0 1-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 0 1-1.45-2.17A6.59 6.59 0 0 1 1.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 0 1 8 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"></path></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input type="text" autocomplete="off" data-no-org-url="/autocomplete/user-suggestions" data-org-url="/suggestions?mention_suggester=1" data-maxlength="80" class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field" placeholder="What&#39;s happening?" name="message" value="" aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden="">
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
            

<div class="d-inline-block f5 mr-2 pt-3 pb-2">
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2019-09-27T12:28:52-04:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2019-09-27T12:58:52-04:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2019-09-27T15:58:52-04:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2019-09-27T23:59:59-04:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2019-09-29T23:59:59-04:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled="" class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled="" class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>


    <a role="menuitem" class="dropdown-item" href="https://github.com/escharf72" data-ga-click="Header, go to profile, text:your profile">Your profile</a>


    <a role="menuitem" class="dropdown-item" href="https://github.com/escharf72?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

    <a role="menuitem" class="dropdown-item" href="https://github.com/escharf72?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="https://github.com/escharf72?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>


    <div role="none" class="dropdown-divider"></div>
    <a role="menuitem" class="dropdown-item" href="https://help.github.com/" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="https://github.com/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --><form class="logout-form" action="https://github.com/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="hIGGjRfxoryZgymP7CmF9WnOtM63XJ5zehIbLq5D+89QgDFuYl9h1v0iOnrwlIJVtkmp09sd7ocrKgpj9sr/fA==">
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
</form>  </details-menu>
</details>

    </div>

  </header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" data-pjax-container="">
      
  

      <div class="border-bottom shelf intro-shelf js-notice mb-0 pb-4">
  <div class="width-full container">
    <div class="width-full mx-auto shelf-content">
      <h2 class="shelf-title">Learn Git and GitHub without any code!</h2>
      <p class="shelf-lead">
          Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
      </p>
      <a class="btn btn-primary shelf-cta" target="_blank" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;READ_GUIDE&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="8c421e7700dc39e9eebb4452d37d00ee4680d2c022891c676465893c1e7f0a71" href="https://guides.github.com/activities/hello-world/">Read the guide</a>
    </div>
    <!-- '"` --><!-- </textarea></xmp> --><form class="shelf-dismiss js-notice-dismiss" action="https://github.com/dashboard/dismiss_bootcamp" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="_method" value="delete"><input type="hidden" name="authenticity_token" value="5JzreV3ovRo3hKBgrCl1LSo382sUQMqP2FEItxC2n1LVPv6yggnkxxrU/lYoQKIjnLLphB+S1Tku/OhmVKf6/g==">
      <button name="button" type="submit" class="mr-1 close-button tooltipped tooltipped-w" aria-label="Hide this notice forever" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;DISMISS_BANNER&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="698fe56ff5dac30ee0a7494fe4bd89e836c94d56cdbd3562f04fbcf5b7619506">
        <svg aria-label="Hide this notice forever" class="octicon octicon-x v-align-text-top" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
</button></form>  </div>
</div>










  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">



    <li hidden="">
      

    </li>

  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --><form data-remote="true" class="clearfix js-social-form js-social-container" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="rpRxB/zE9aigu/2nFtCh+fEYuxYLA9o/nG/dpQvSsBP+mUhUepWTlcUEcqAgc3Z4xv2es4el+vu599tyGVHGdA==">      <input type="hidden" name="repository_id" value="206609099">

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="62a858654555e70fd518a2861d97780dea2a8a02a246e31836c120f0bffabfb4" data-ga-click="Repository, click Watch settings, action:files#disambiguate" aria-haspopup="menu" role="button">          <span data-menu-button="">
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
              Unwatch
          </span>
</summary>        <details-menu class="select-menu-modal position-absolute mt-5" style="z-index: 99;" role="menu">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents="">
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents="">
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents="">
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents="">
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"></path></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count" href="https://github.com/escharf72/CircuitPython/watchers" aria-label="1 user is watching this repository">
          1
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --><form class="starred js-social-form" action="https://github.com/escharf72/CircuitPython/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="AsWq9uikBZ+oUzauygyS5fwhsbR9iEef2IifSZiUI/RmqQef1duXXIb9cC3rL71xmTpv/1DfdeGD+rroAL/22g==">
      <input type="hidden" name="context" value="repository">
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar escharf72/CircuitPython" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="ab5dbfd105b72455adff7b07fd6ace2533d2da6f144c8be617af5642ec543fa2" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"></path></svg>
        Unstar
</button>        <a class="social-count js-social-count" href="https://github.com/escharf72/CircuitPython/stargazers" aria-label="0 users starred this repository">
           0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --><form class="unstarred js-social-form" action="https://github.com/escharf72/CircuitPython/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="JxuWt1hKHzE98/R5iTt91KhYQxvojwRLzbszG98y5BGKL8P6vMMWRnJKkuuC43sJFslT8Ow/AYYr5iu8h1hfTw==">
      <input type="hidden" name="context" value="repository">
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star escharf72/CircuitPython" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="c82fac38247814b424ccc219c2f7d7e82a48da99ccfadd3fcf2bf3568bb8eebe" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"></path></svg>
        Star
</button>        <a class="social-count js-social-count" href="https://github.com/escharf72/CircuitPython/stargazers" aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
        <span class="btn btn-sm btn-with-count disabled tooltipped tooltipped-sw" aria-label="Cannot fork because you own this repository and are not a member of any organizations.">
          <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
          Fork
</span>
    <a href="https://github.com/escharf72/CircuitPython/network/members" class="social-count" aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

      <h1 class="public ">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=54952359" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/escharf72">escharf72</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="https://github.com/escharf72/CircuitPython">CircuitPython</a></strong>
  

</h1>

    </div>
    
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container" itemscope="" itemtype="http://schema.org/BreadcrumbList" aria-label="Repository" data-pjax="#js-repo-pjax-container">

  <span itemscope="" itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /escharf72/CircuitPython" href="https://github.com/escharf72/CircuitPython">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope="" itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /escharf72/CircuitPython/issues" href="https://github.com/escharf72/CircuitPython/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope="" itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /escharf72/CircuitPython/pulls" href="https://github.com/escharf72/CircuitPython/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /escharf72/CircuitPython/projects" href="https://github.com/escharf72/CircuitPython/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"></path></svg>
      Projects
      <span class="Counter">0</span>
</a>

    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /escharf72/CircuitPython/wiki" href="https://github.com/escharf72/CircuitPython/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"></path></svg>
      Wiki
</a>
    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /escharf72/CircuitPython/network/alerts" href="https://github.com/escharf72/CircuitPython/network/alerts">
      <svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"></path></svg>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /escharf72/CircuitPython/pulse" href="https://github.com/escharf72/CircuitPython/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg>
      Insights
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations repo_keys_settings issue_template_editor secrets_settings key_links_settings /escharf72/CircuitPython/settings" href="https://github.com/escharf72/CircuitPython/settings">
      <svg class="octicon octicon-gear" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"></path></svg>
      Settings
</a>
</nav>


  </div>
<div class="container-lg clearfix new-discussion-timeline experiment-repo-nav  px-3">
  <div class="repository-content ">

    
    
    

      <details id="repo-meta-edit" class="Details-element details-reset js-dropdown-details ">
    <summary class="d-block">
      <div class="Details-content--closed f4">
        <div class="d-flex flex-items-start">
          <span class="flex-auto mb-2">  <div class="f4">
        <em class="d-block text-gray">
          No description, website, or topics provided.
        </em>
  </div>
</span>
          <span class="btn btn-sm">Edit</span>
        </div>
      </div>
      <div class="Details-content--open sr-only">Cancel edit description</div>
    </summary>
      <!-- '"` --><!-- </textarea></xmp> --><form class="flex-items-end d-flex f6 mb-3 pb-3 border-bottom js-edit-repository-meta" action="https://github.com/escharf72/CircuitPython/settings/update_meta" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="_method" value="put"><input type="hidden" name="authenticity_token" value="PiSQFtZq7gEu3xdBNYRNwdnx9tBDoKHbtDCNdNj9/ACOVzVAIKhj4kF81WEfDoDYXXJloBXWGKb+Q6A1w+dROg==">
        <div class="flex-auto col-6 mr-2">
          <label for="repo_description">Description</label>
          <input type="text" id="repo_description" class="form-control input-contrast mt-1 width-full" name="repo_description" value="" placeholder="Short description of this repository" autofocus="">
        </div>
        <div class="flex-auto mr-2">
          <label for="repo_homepage">Website</label>
          <input type="url" id="repo_homepage" class="form-control input-contrast mt-1 width-full" name="repo_homepage" value="" placeholder="Website for this repository (optional)">
        </div>
        <div class="no-wrap">
          <button class="btn" type="submit">Save</button>
          or <button type="button" class="btn-link" data-toggle-for="repo-meta-edit">Cancel</button>
        </div>
</form>  </details>

    <details id="topics-list-container" class="Details-element details-reset mb-2 d-inline-block js-dropdown-details repository-topics-container" data-deferred-details-content-url="/escharf72/CircuitPython/settings/edit_topics">
      <summary>
        <div class="Details-content--closed">
          <span class="js-topics-list-container mb-1 float-left" data-url="/escharf72/CircuitPython/settings/topics">
            
          </span>
          <span class="btn-link f6 mb-2">Manage topics</span>
        </div>
        <div class="Details-content--open sr-only">Cancel manage topics</div>
      </summary>
      <include-fragment class="my-2"><img alt="Loading" src="./hello_vs_code_files/octocat-spinner-32.gif" width="32" height="32"></include-fragment>
    </details>



  <div class="overall-summary overall-summary-bottomless">
    <ul class="numbers-summary">
      <li class="commits">
        <a data-pjax="" href="https://github.com/escharf72/CircuitPython/commits/master">
            <svg class="octicon octicon-history" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z"></path></svg>
            <span class="num text-emphasized">
              7
            </span>
            commits
        </a>
      </li>
      <li>
        <a data-pjax="" href="https://github.com/escharf72/CircuitPython/branches">
          <svg class="octicon octicon-git-branch" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
          <span class="num text-emphasized">
            1
          </span>
          branch
        </a>
      </li>


      <li>
        <a href="https://github.com/escharf72/CircuitPython/releases">
          <svg class="octicon octicon-tag" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.73 1.73C7.26 1.26 6.62 1 5.96 1H3.5C2.13 1 1 2.13 1 3.5v2.47c0 .66.27 1.3.73 1.77l6.06 6.06c.39.39 1.02.39 1.41 0l4.59-4.59a.996.996 0 0 0 0-1.41L7.73 1.73zM2.38 7.09c-.31-.3-.47-.7-.47-1.13V3.5c0-.88.72-1.59 1.59-1.59h2.47c.42 0 .83.16 1.13.47l6.14 6.13-4.73 4.73-6.13-6.15zM3.01 3h2v2H3V3h.01z"></path></svg>
          <span class="num text-emphasized">
            0
          </span>
          releases
        </a>
      </li>


        <li data-contributors-hovercards-enabled="">
            <a href="https://github.com/escharf72/CircuitPython/graphs/contributors" data-hovercard-type="contributors" data-hovercard-url="/escharf72/CircuitPython/community_contributors/hovercard">
  <svg class="octicon octicon-organization" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 12.999c0 .439-.45 1-1 1H7.995c-.539 0-.994-.447-.995-.999H1c-.54 0-1-.561-1-1 0-2.634 3-4 3-4s.229-.409 0-1c-.841-.621-1.058-.59-1-3 .058-2.419 1.367-3 2.5-3s2.442.58 2.5 3c.058 2.41-.159 2.379-1 3-.229.59 0 1 0 1s1.549.711 2.42 2.088C9.196 9.369 10 8.999 10 8.999s.229-.409 0-1c-.841-.62-1.058-.59-1-3 .058-2.419 1.367-3 2.5-3s2.437.581 2.495 3c.059 2.41-.158 2.38-1 3-.229.59 0 1 0 1s3.005 1.366 3.005 4z"></path></svg>
    <span class="num text-emphasized">
      0
    </span>
    contributors
</a>        </li>

    </ul>
  </div>

    <details class="details-reset">
      <summary title="Click for language details" data-ga-click="Repository, language bar stats toggle, location:repo overview">
        <div class="d-flex repository-lang-stats-graph">
            <span class="language-color" aria-label="Python 100.0%" style="width:100.0%; background-color:#3572A5;" itemprop="keywords">Python</span>
        </div>
      </summary>
      <div class="repository-lang-stats">
        <ol class="repository-lang-stats-numbers">
          <li>
              <a href="https://github.com/escharf72/CircuitPython/search?l=python" data-ga-click="Repository, language stats search click, location:repo overview">
                <span class="color-block language-color" style="background-color:#3572A5;"></span>
                <span class="lang">Python</span>
                <span class="percent">100.0%</span>
              </a>
          </li>
        </ol>
      </div>
    </details>





    <div class="mt-2">
        <div class="js-socket-channel js-updatable-content" data-channel="repo:206609099:post-receive:54952359" data-url="/escharf72/CircuitPython/show_partial?partial=tree%2Frecently_touched_branches_list">
  </div>

    </div>

  <div class="file-navigation in-mid-page d-flex flex-items-start">
  
<details class="details-reset details-overlay select-menu branch-select-menu  hx_rsm" id="branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate" data-hotkey="w" title="Switch branches or tags" aria-haspopup="menu" role="button">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button="">master</span>
  </summary>

  <details-menu class="select-menu-modal hx_rsm-modal position-absolute" style="z-index: 99;" src="/escharf72/CircuitPython/ref-list/master?source_action=disambiguate&amp;source_controller=files" preload="" role="menu">
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"></path></svg>
    </include-fragment>
  </details-menu>
</details>


        <a class="btn btn-sm new-pull-request-btn" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;NEW_PULL_REQUEST_BUTTON&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="8fb6fa94983c41c2530c18ac1b880096d230658257c22aa66fa6471c5d0a11f2" data-ga-click="Repository, new pull request, location:repo overview" data-pjax="true" href="https://github.com/escharf72/CircuitPython/pull/new/master">New pull request</a>

  <div class="breadcrumb flex-auto">
    
  </div>

  <div class="BtnGroup">
      
  <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent" action="https://github.com/escharf72/CircuitPython/new/master" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="CpEECKZgKKCCxOqCCawOw9KNoW6A2wasF5x4Hwa3GBSR13pE5wXS0d36OVVwptIxObVotDPze0QK2Lxm+G3RWQ==">
    <button class="btn btn-sm BtnGroup-item" type="submit" data-disable-with="Creating file…">
      Create new file
    </button>
</form>

      
  <a href="https://github.com/escharf72/CircuitPython/upload/master" class="btn btn-sm BtnGroup-item">
    Upload files
  </a>


      <a class="btn btn-sm empty-icon BtnGroup-item d-none" data-hotkey="F" href="https://github.com/escharf72/CircuitPython/search_pilot">Search Code</a>

    <a class="btn btn-sm empty-icon float-right BtnGroup-item" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="e4312382dea257325e20dd8452f7da15343e34c1b7b38b629cdd85431443ee41" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-pjax="true" href="https://github.com/escharf72/CircuitPython/find/master">Find File</a>
  </div>


    

    <details class="get-repo-select-menu js-get-repo-select-menu  position-relative details-overlay details-reset">
  <summary class="btn btn-sm ml-2 btn-primary" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:206609099,&quot;target&quot;:&quot;CLONE_OR_DOWNLOAD_BUTTON&quot;,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="bc5db14b652877c4301798cb3727b465534b956c91f5c5ee114e59f1014a27b3">
    Clone or download
    <span class="dropdown-caret"></span>
</summary>  <div class="position-relative">
    <div class="get-repo-modal dropdown-menu dropdown-menu-sw pb-0 js-toggler-container  js-get-repo-modal">

      <div class="get-repo-modal-options">
          <div class="clone-options https-clone-options">
              <!-- '"` --><!-- </textarea></xmp> --><form data-remote="true" action="https://github.com/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="ePLbLFmE/ng3cLhEqS+Yt4+V6aYVKJzfq9LueUqsjo44g6n4fiSC6lm01od6p0StFczlGL8pdKYVzT4bMeOZew=="><button name="button" type="submit" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_SSH&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="f11bcf5d298c6bb6e175ffad16c0d98394cd33b96174afc72c44168dd1a9a5ad" class="btn-link btn-change-protocol js-toggler-target float-right">Use SSH</button></form>

            <h4 class="mb-1">
              Clone with HTTPS
              <a class="muted-link" href="https://help.github.com/articles/which-remote-url-should-i-use" target="_blank" title="Which remote URL should I use?">
                <svg class="octicon octicon-question" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6 10h2v2H6v-2zm4-3.5C10 8.64 8 9 8 9H6c0-.55.45-1 1-1h.5c.28 0 .5-.22.5-.5v-1c0-.28-.22-.5-.5-.5h-1c-.28 0-.5.22-.5.5V7H4c0-1.5 1.5-3 3-3s3 1 3 2.5zM7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7z"></path></svg>
              </a>
            </h4>
            <p class="mb-2 get-repo-decription-text">
              Use Git or checkout with SVN using the web URL.
            </p>

            <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm" data-autoselect="" value="https://github.com/escharf72/CircuitPython.git" aria-label="Clone this repository at https://github.com/escharf72/CircuitPython.git" readonly="">
  <div class="input-group-button">
    <clipboard-copy value="https://github.com/escharf72/CircuitPython.git" aria-label="Copy to clipboard" class="btn btn-sm" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="fbd0724d7e487786f896c5f4e5299c6080022018d126f503ba598b598bed011d" tabindex="0" role="button"><svg class="octicon octicon-clippy" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"></path></svg></clipboard-copy>
  </div>
</div>

          </div>

          <div class="clone-options ssh-clone-options">
              <!-- '"` --><!-- </textarea></xmp> --><form data-remote="true" action="https://github.com/users/set_protocol?protocol_selector=https&amp;protocol_type=push" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="g8SSz3R1IWgOWsm4bPuJy0fTkl4oNvGdE68h9ldCdjrDteAbU9Vd+mCep3u/c1XR3Yqe4II3GeStsPGULA1hzw=="><button name="button" type="submit" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_HTTPS&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="3df98c8387a70030841f39ba8e51b8a2f9fea530b2234b5499800e9907a7fb57" class="btn-link btn-change-protocol js-toggler-target float-right">Use HTTPS</button></form>
              <h4 class="mb-1">
                Clone with SSH
                <a class="muted-link" href="https://help.github.com/articles/which-remote-url-should-i-use" target="_blank" title="Which remote URL should I use?">
                  <svg class="octicon octicon-question" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6 10h2v2H6v-2zm4-3.5C10 8.64 8 9 8 9H6c0-.55.45-1 1-1h.5c.28 0 .5-.22.5-.5v-1c0-.28-.22-.5-.5-.5h-1c-.28 0-.5.22-.5.5V7H4c0-1.5 1.5-3 3-3s3 1 3 2.5zM7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7z"></path></svg>
                </a>
              </h4>

                <div class="flash flash-warn my-3">
                  You don't have any public SSH keys in your GitHub account.
                  You can <a href="https://github.com/settings/ssh/new">add a new public key</a>, or try cloning this repository via <button class="btn-link js-toggler-target">HTTPS.</button>
                </div>

              <p class="mb-2 get-repo-decription-text">
                  Use a password protected SSH key.
              </p>

              <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm" data-autoselect="" value="git@github.com:escharf72/CircuitPython.git" aria-label="Clone this repository at git@github.com:escharf72/CircuitPython.git" readonly="">
  <div class="input-group-button">
    <clipboard-copy value="git@github.com:escharf72/CircuitPython.git" aria-label="Copy to clipboard" class="btn btn-sm" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="fbd0724d7e487786f896c5f4e5299c6080022018d126f503ba598b598bed011d" tabindex="0" role="button"><svg class="octicon octicon-clippy" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"></path></svg></clipboard-copy>
  </div>
</div>

          </div>
        <div class="mt-2">
            <a class="btn btn-outline get-repo-btn tooltipped tooltipped-s tooltipped-multiline js-get-repo" aria-label="Clone escharf72/CircuitPython to your computer and use it in GitHub Desktop." data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;OPEN_IN_DESKTOP&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="4b61e9d4fefdae7e862a5f0e4cc03e51b915a4319cc539e99f3ba38944bb8b9e" data-open-app="windows" href="https://desktop.github.com/">Open in Desktop</a>

<a class="btn btn-outline get-repo-btn  " rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;DOWNLOAD_ZIP&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:206609099,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="48e6a2729de638c905e15ca63091433a1b19322e48cf6f3f9da72d08f9ec31f4" data-ga-click="Repository, download zip, location:repo overview" href="https://github.com/escharf72/CircuitPython/archive/master.zip">Download ZIP</a>

        </div>
      </div>


      <div class="js-modal-download-mac py-2 px-3 d-none">
        <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
        <p class="text-gray">If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.</p>
        <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
      </div>

      <div class="js-modal-download-windows py-2 px-3 d-none">
        <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
        <p class="text-gray">If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.</p>
        <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
      </div>

      <div class="js-modal-download-xcode py-2 px-3 d-none">
        <h4 class="lh-condensed mb-3">Launching Xcode<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
        <p class="text-gray">If nothing happens, <a href="https://developer.apple.com/xcode/">download Xcode</a> and try again.</p>
        <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
      </div>

      <div class="js-modal-download-visual-studio py-2 px-3 d-none">
        <h4 class="lh-condensed mb-3">Launching Visual Studio<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
        <p class="text-gray">If nothing happens, <a href="https://visualstudio.github.com/">download the GitHub extension for Visual Studio</a> and try again.</p>
        <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
      </div>

    </div>
  </div>
</details>

</div>


  


  <div class="commit-tease js-details-container Details d-flex rounded-top-1" data-issue-and-pr-hovercards-enabled="">
    
<div class="AvatarStack flex-self-start ">
  <div class="AvatarStack-body" aria-label="Elisabeth A Scharf">
        <img src="./hello_vs_code_files/68747470733a2f2f312e67726176617461722e636f6d2f6176617461722f39626131643064633632386132323832316262333636633037353833616265643f643d68747470732533412532462532466769746875622e6769746875626173736574732e636f6d253246" width="20" height="20" class="avatar" alt="Elisabeth A Scharf">
  </div>
</div>

    <div class="flex-auto f6 mr-3">
      
        <span class="commit-author user-mention">Elisabeth A Scharf</span>


  


        <a data-pjax="true" title="&quot;Add hello_vs_code.py&quot;" class="message text-inherit" href="https://github.com/escharf72/CircuitPython/commit/cada4e4d97ed37618145b86cb0fc5f5e9a84cac4">"Add hello_vs_code.py"</a>

    </div>
    <div class="no-wrap d-flex flex-items-baseline">
      <span class="mr-1">Latest commit</span>
      <a class="commit-tease-sha mr-1" href="https://github.com/escharf72/CircuitPython/commit/cada4e4d97ed37618145b86cb0fc5f5e9a84cac4" data-pjax="">
        cada4e4
      </a>
      <span itemprop="dateModified"><relative-time datetime="2019-09-27T15:57:36Z" title="Sep 27, 2019, 11:57 AM EDT">1 minute ago</relative-time></span>
    </div>
  </div>





<div class="file-wrap">
  <a class="d-none js-permalink-shortcut" data-hotkey="y" href="https://github.com/escharf72/CircuitPython/tree/cada4e4d97ed37618145b86cb0fc5f5e9a84cac4">Permalink</a>

  <table class="files js-navigation-container js-active-navigation-container" data-pjax="">
    <thead>
      <tr>
        <th><span class="sr-only">Type</span></th>
        <th><span class="sr-only">Name</span></th>
        <th><span class="sr-only">Latest commit message</span></th>
        <th><span class="sr-only">Commit time</span></th>
      </tr>
    </thead>


    <tbody>
      <tr class="warning include-fragment-error">
        <td class="icon"><svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"></path></svg></td>
        <td class="content" colspan="3">Failed to load latest commit information.</td>
      </tr>

        <tr class="js-navigation-item navigation-focus" aria-selected="true">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="Engineering3_CircuitPython_LCDscreen_EAS.py" id="acd335bed91134bd5eedf7fcf01f72e5-c0979c9a360efdfdce76fc4c88fee38b54ac2242" href="https://github.com/escharf72/CircuitPython/blob/master/Engineering3_CircuitPython_LCDscreen_EAS.py">Engineering3_CircuitPython_LCDscreen_EAS.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding first five CircuitPython assignment files" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/e533b6ea890dbd6aad7dabb6d64918eb58568a2a">Adding first five CircuitPython assignment files</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-05T16:12:36Z" title="Sep 5, 2019, 12:12 PM EDT">22 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="Engineering3_CircuitPython_LEDfade_EAS.py" id="8460ac424e34b168da6979f4cb6033d4-ebc73c865b7d21bdf9647df7548d1a07b58c2e14" href="https://github.com/escharf72/CircuitPython/blob/master/Engineering3_CircuitPython_LEDfade_EAS.py">Engineering3_CircuitPython_LEDfade_EAS.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding first five CircuitPython assignment files" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/e533b6ea890dbd6aad7dabb6d64918eb58568a2a">Adding first five CircuitPython assignment files</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-05T16:12:36Z" title="Sep 5, 2019, 12:12 PM EDT">22 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="Engineering3_CircuitPython_Photointerrupter_EAS.py" id="0d4d17f4b96126e9e2f2739a11147b60-5268638dca288d098f315f8b07229a8e5c90988e" href="https://github.com/escharf72/CircuitPython/blob/master/Engineering3_CircuitPython_Photointerrupter_EAS.py">Engineering3_CircuitPython_Photointerrupter_EAS.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding first five CircuitPython assignment files" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/e533b6ea890dbd6aad7dabb6d64918eb58568a2a">Adding first five CircuitPython assignment files</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-05T16:12:36Z" title="Sep 5, 2019, 12:12 PM EDT">22 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="Engineering3_CircuitPython_ServoAssignment_EAS.py" id="cc091dd3ccee9687face06d5410ed1ce-49bd3177866bc02e1b21af7b6b5ee8d2568fe137" href="https://github.com/escharf72/CircuitPython/blob/master/Engineering3_CircuitPython_ServoAssignment_EAS.py">Engineering3_CircuitPython_ServoAssignment_EAS.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding first five CircuitPython assignment files" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/e533b6ea890dbd6aad7dabb6d64918eb58568a2a">Adding first five CircuitPython assignment files</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-05T16:12:36Z" title="Sep 5, 2019, 12:12 PM EDT">22 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="README.md" id="04c6e90faac2675aa89e2176d2eec7d8-b115e08aee8391d1af44231408f783dd04a5eaeb" href="https://github.com/escharf72/CircuitPython/blob/master/README.md">README.md</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Still editing my README file" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/fcf38268e0c3cfc9d17abb8c307565fa611f35eb">Still editing my README file</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-25T15:22:02Z" title="Sep 25, 2019, 11:22 AM EDT">2 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="RGB_code.py" id="531b068075e036157f06674649a806a0-8a62fc6b25fffe9e50620fcaef640293f41f2892" href="https://github.com/escharf72/CircuitPython/blob/master/RGB_code.py">RGB_code.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding new files from another Circuit Python assignment

git status

git status" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/3710b8fb8791fc63fefde6e39249e23b3fe41ea1">Adding new files from another Circuit Python assignment</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-25T14:57:25Z" title="Sep 25, 2019, 10:57 AM EDT">2 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="hello_vs_code.py" id="d4a97bc079b0fe2269d53bdd5d042870-1a941f7a999b02f295508559cd15ca01397957d6" href="https://github.com/escharf72/CircuitPython/blob/master/hello_vs_code.py">hello_vs_code.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="&quot;Add hello_vs_code.py&quot;" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/cada4e4d97ed37618145b86cb0fc5f5e9a84cac4">"Add hello_vs_code.py"</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-27T15:57:36Z" title="Sep 27, 2019, 11:57 AM EDT">1 minute ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="main.py" id="5bc02cefb3ea9e27f1a6776eabd1935d-5268638dca288d098f315f8b07229a8e5c90988e" href="https://github.com/escharf72/CircuitPython/blob/master/main.py">main.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding first five CircuitPython assignment files" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/e533b6ea890dbd6aad7dabb6d64918eb58568a2a">Adding first five CircuitPython assignment files</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-05T16:12:36Z" title="Sep 5, 2019, 12:12 PM EDT">22 days ago</time-ago></span>
          </td>
        </tr>
        <tr class="js-navigation-item" aria-selected="false">
          <td class="icon">
            <svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
            <img width="16" height="16" class="spinner" alt="" src="./hello_vs_code_files/octocat-spinner-32.gif">
          </td>
          <td class="content">
            <span class="css-truncate css-truncate-target"><a class="js-navigation-open" title="rgb.py" id="5aae9f9c93c040862c14bff57a271e41-d311cc88b0b7b330db3623d039f7e432c3eb8ac8" href="https://github.com/escharf72/CircuitPython/blob/master/rgb.py">rgb.py</a></span>
          </td>
          <td class="message">
            <span class="css-truncate css-truncate-target">
                  <a data-pjax="true" title="Adding new files from another Circuit Python assignment

git status

git status" class="link-gray" href="https://github.com/escharf72/CircuitPython/commit/3710b8fb8791fc63fefde6e39249e23b3fe41ea1">Adding new files from another Circuit Python assignment</a>
            </span>
          </td>
          <td class="age">
            <span class="css-truncate css-truncate-target"><time-ago datetime="2019-09-25T14:57:25Z" title="Sep 25, 2019, 10:57 AM EDT">2 days ago</time-ago></span>
          </td>
        </tr>
    </tbody>
  </table>

</div>

  <div class="repo-file-upload-tree-target js-document-dropzone js-upload-manifest-tree-view" data-drop-url="/escharf72/CircuitPython/upload/master" data-directory-upload="">
    <div class="repo-file-upload-outline">
      <div class="repo-file-upload-slate">
          <svg width="204" height="52" viewBox="0 0 204 52" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g class="files-lg" fill="#717171">
              <path class="file-graph" d="M40,42 L40,12 L42,12 L42,40 L64,40 L64,42 L40,42 L40,42 Z M45,37 L45,16 L49,16 L49,37 L45,37 L45,37 Z M51,37 L51,22 L55,22 L55,37 L51,37 L51,37 Z M68.5,48 L35.5,48 C34.7,48 34,47.3 34,46.5 L34,7.5 C34,6.7 34.7,6 35.5,6 L59,6 L70,17 L70,46.5 C70,47.3 69.3,48 68.5,48 L68.5,48 Z M68,18 L58,8 L36,8 L36,46 L68,46 L68,18 L68,18 Z M57,37 L57,27 L61,27 L61,37 L57,37 L57,37 Z"></path>
              <path class="file-zip" d="M17,14 L1,14 C0.4,14 0,14.5 0,15 L0,41 C0,41.5 0.4,42 1,42 L23,42 C23.6,42 24,41.5 24,41 L24,21 L17,14 Z M22,40 L2,40 L2,16 L8,16 L8,18 L10,18 L10,16 L16,16 L22,22 L22,40 Z M8,30.5 C6.8,31.2 6,32.5 6,34 L6,36 L14,36 L14,34 C14,31.8 12.2,30 10,30 L10,28 L8,28 L8,30.5 Z M12,32 L12,34 L8,34 L8,32 L12,32 Z M10,20 L10,18 L12,18 L12,20 L10,20 Z M8,20 L10,20 L10,22 L8,22 L8,20 Z M10,24 L10,22 L12,22 L12,24 L10,24 Z M8,24 L10,24 L10,26 L8,26 L8,24 Z M10,28 L10,26 L12,26 L12,28 L10,28 Z"></path>
              <path class="file-generic" d="M168.5,48 L135.5,48 C134.7,48 134,47.3 134,46.5 L134,7.5 C134,6.7 134.7,6 135.5,6 L159,6 L170,17 L170,46.5 C170,47.3 169.3,48 168.5,48 Z M168,18 L158,8 L136,8 L136,46 L168,46 L168,18 Z M140,35 L140,33 L161,33 L161,35 L140,35 Z M140,30 L140,28 L161,28 L161,30 L140,30 Z M140,25 L140,23 L161,23 L161,25 L140,25 Z M140,17 L140,15 L152,15 L152,17 L140,17 Z M140,40 L140,38 L161,38 L161,40 L140,40 Z"></path>
              <path class="file-acrobat" d="M181,14 C180.5,14 180,14.5 180,15 L180,41 C180,41.5 180.5,42 181,42 L203,42 C203.5,42 204,41.5 204,41 L204,23 L204,21 L197,14 L181,14 Z M200.8,29.9 C200.3,29.8 199.8,29.7 199.3,29.7 C198.5,29.7 197.7,29.8 196.8,29.9 C196.3,29.8 195.7,29.3 194.8,28.6 C193.9,27.9 193.1,26.3 192.2,23.9 C192.5,22.2 192.6,20.9 192.7,19.9 C192.8,18.9 192.8,18.4 192.7,18.4 C192.8,17.6 192.6,17 192.3,16.6 C192,16.2 191.4,16 191,16 L196,16 L202,22 L202,30.4 C201.6,30.2 201.2,30 200.8,29.9 Z M182,16 L190,16 C189.8,16.1 189.6,16.2 189.4,16.4 C189.2,16.6 189,16.9 188.9,17.4 C188.7,18.2 188.6,19.2 188.7,20.3 C188.8,21.5 189.1,22.7 189.4,23.9 C188.9,25.4 188.2,27.2 187.2,29.3 C186.2,31.4 185.6,32.6 185.4,33 C185.1,33.1 184.7,33.3 184,33.6 C183.3,33.9 182.7,34.4 182,35 L182,16 L182,16 Z M195.1,31 C193.8,31.2 192.6,31.4 191.5,31.7 C190.3,32 189.1,32.4 187.8,32.9 L189,30.4 C189.8,28.7 190.4,27.2 190.8,25.8 L190.8,25.9 C191.7,28.2 192.5,29.6 193.1,30.1 C193.8,30.5 194.5,30.8 195.1,31 L195.1,31 Z M184.1,39.2 C185,38.4 186.2,36.9 187.7,34.4 C188.3,34.1 188.9,33.9 189.3,33.7 L190.1,33.4 C191.1,33.1 192,32.9 193,32.7 C194,32.5 195,32.4 196,32.3 C196.9,32.7 197.9,33.1 198.8,33.3 C199.8,33.6 200.6,33.7 201.3,33.8 C201.5,33.8 201.8,34 202,34 L202,40 L182,40 C182.4,39.9 183.6,39.6 184.1,39.2 Z"></path>
              <path class="file-code" d="M111,0 L82,0 C80.9,0 80,0.9 80,2 L80,50 C80,51.1 80.9,52 82,52 L122,52 C123.1,52 124,51.1 124,50 L124,13 L111,0 Z M122,50 L82,50 L82,2 L110,2 L122,14 L122,50 Z M107,18 L116,28 L107,38 L104,35 L111,28 L104,21 L107,18 Z M100,21 L93,28 L100,35 L97,38 L88,28 L97,18 L100,21 Z"></path>
            </g>
          </svg>

          <h2>Drop to upload your files</h2>
      </div>
    </div>
  </div>


  <div class="repo-file-upload-tree-target js-document-dropzone js-upload-manifest-tree-view" data-drop-url="/escharf72/CircuitPython/upload/master" data-directory-upload="">
    <div class="repo-file-upload-outline">
      <div class="repo-file-upload-slate">
          <svg width="204" height="52" viewBox="0 0 204 52" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g class="files-lg" fill="#717171">
              <path class="file-graph" d="M40,42 L40,12 L42,12 L42,40 L64,40 L64,42 L40,42 L40,42 Z M45,37 L45,16 L49,16 L49,37 L45,37 L45,37 Z M51,37 L51,22 L55,22 L55,37 L51,37 L51,37 Z M68.5,48 L35.5,48 C34.7,48 34,47.3 34,46.5 L34,7.5 C34,6.7 34.7,6 35.5,6 L59,6 L70,17 L70,46.5 C70,47.3 69.3,48 68.5,48 L68.5,48 Z M68,18 L58,8 L36,8 L36,46 L68,46 L68,18 L68,18 Z M57,37 L57,27 L61,27 L61,37 L57,37 L57,37 Z"></path>
              <path class="file-zip" d="M17,14 L1,14 C0.4,14 0,14.5 0,15 L0,41 C0,41.5 0.4,42 1,42 L23,42 C23.6,42 24,41.5 24,41 L24,21 L17,14 Z M22,40 L2,40 L2,16 L8,16 L8,18 L10,18 L10,16 L16,16 L22,22 L22,40 Z M8,30.5 C6.8,31.2 6,32.5 6,34 L6,36 L14,36 L14,34 C14,31.8 12.2,30 10,30 L10,28 L8,28 L8,30.5 Z M12,32 L12,34 L8,34 L8,32 L12,32 Z M10,20 L10,18 L12,18 L12,20 L10,20 Z M8,20 L10,20 L10,22 L8,22 L8,20 Z M10,24 L10,22 L12,22 L12,24 L10,24 Z M8,24 L10,24 L10,26 L8,26 L8,24 Z M10,28 L10,26 L12,26 L12,28 L10,28 Z"></path>
              <path class="file-generic" d="M168.5,48 L135.5,48 C134.7,48 134,47.3 134,46.5 L134,7.5 C134,6.7 134.7,6 135.5,6 L159,6 L170,17 L170,46.5 C170,47.3 169.3,48 168.5,48 Z M168,18 L158,8 L136,8 L136,46 L168,46 L168,18 Z M140,35 L140,33 L161,33 L161,35 L140,35 Z M140,30 L140,28 L161,28 L161,30 L140,30 Z M140,25 L140,23 L161,23 L161,25 L140,25 Z M140,17 L140,15 L152,15 L152,17 L140,17 Z M140,40 L140,38 L161,38 L161,40 L140,40 Z"></path>
              <path class="file-acrobat" d="M181,14 C180.5,14 180,14.5 180,15 L180,41 C180,41.5 180.5,42 181,42 L203,42 C203.5,42 204,41.5 204,41 L204,23 L204,21 L197,14 L181,14 Z M200.8,29.9 C200.3,29.8 199.8,29.7 199.3,29.7 C198.5,29.7 197.7,29.8 196.8,29.9 C196.3,29.8 195.7,29.3 194.8,28.6 C193.9,27.9 193.1,26.3 192.2,23.9 C192.5,22.2 192.6,20.9 192.7,19.9 C192.8,18.9 192.8,18.4 192.7,18.4 C192.8,17.6 192.6,17 192.3,16.6 C192,16.2 191.4,16 191,16 L196,16 L202,22 L202,30.4 C201.6,30.2 201.2,30 200.8,29.9 Z M182,16 L190,16 C189.8,16.1 189.6,16.2 189.4,16.4 C189.2,16.6 189,16.9 188.9,17.4 C188.7,18.2 188.6,19.2 188.7,20.3 C188.8,21.5 189.1,22.7 189.4,23.9 C188.9,25.4 188.2,27.2 187.2,29.3 C186.2,31.4 185.6,32.6 185.4,33 C185.1,33.1 184.7,33.3 184,33.6 C183.3,33.9 182.7,34.4 182,35 L182,16 L182,16 Z M195.1,31 C193.8,31.2 192.6,31.4 191.5,31.7 C190.3,32 189.1,32.4 187.8,32.9 L189,30.4 C189.8,28.7 190.4,27.2 190.8,25.8 L190.8,25.9 C191.7,28.2 192.5,29.6 193.1,30.1 C193.8,30.5 194.5,30.8 195.1,31 L195.1,31 Z M184.1,39.2 C185,38.4 186.2,36.9 187.7,34.4 C188.3,34.1 188.9,33.9 189.3,33.7 L190.1,33.4 C191.1,33.1 192,32.9 193,32.7 C194,32.5 195,32.4 196,32.3 C196.9,32.7 197.9,33.1 198.8,33.3 C199.8,33.6 200.6,33.7 201.3,33.8 C201.5,33.8 201.8,34 202,34 L202,40 L182,40 C182.4,39.9 183.6,39.6 184.1,39.2 Z"></path>
              <path class="file-code" d="M111,0 L82,0 C80.9,0 80,0.9 80,2 L80,50 C80,51.1 80.9,52 82,52 L122,52 C123.1,52 124,51.1 124,50 L124,13 L111,0 Z M122,50 L82,50 L82,2 L110,2 L122,14 L122,50 Z M107,18 L116,28 L107,38 L104,35 L111,28 L104,21 L107,18 Z M100,21 L93,28 L100,35 L97,38 L88,28 L97,18 L100,21 Z"></path>
            </g>
          </svg>

          <h2>Drop to upload your files</h2>
      </div>
    </div>
  </div>


  <div id="readme" class="Box Box--condensed instapaper_body md js-code-block-container">
    <div class="Box-header d-flex flex-items-center flex-justify-between px-2">
      <h3 class="Box-title pr-3">
        <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"></path></svg>
        README.md
      </h3>
        <div>
            <a href="https://github.com/escharf72/CircuitPython/edit/master/README.md" class="Box-btn-octicon btn-octicon float-right" aria-label="Edit this file"><svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg></a>
        </div>
    </div>
        <div class="Popover anim-scale-in js-tagsearch-popover" hidden="" data-tagsearch-url="/escharf72/CircuitPython/find-symbols" data-tagsearch-ref="master" data-tagsearch-path="README.md" data-tagsearch-lang="Markdown" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:206609099,&quot;ref&quot;:&quot;master&quot;,&quot;client_id&quot;:&quot;1963930123.1566489105&quot;,&quot;originating_request_id&quot;:&quot;E9D4:07B5:50D56D:7E91E7:5D8E31B9&quot;,&quot;originating_url&quot;:&quot;https://github.com/escharf72/CircuitPython&quot;,&quot;referrer&quot;:&quot;https://github.com/escharf72&quot;,&quot;user_id&quot;:54952359}}" data-hydro-click-hmac="16eb8815e2e52e4ffd9fe0c907740d87f744db21a5aa24db04040edf3beeebe3">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>

      <div class="Box-body">
        <article class="markdown-body entry-content p-5" itemprop="text"><h1><a id="user-content-circuit-python" class="anchor" aria-hidden="true" href="https://github.com/escharf72/CircuitPython#circuit-python"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Circuit Python</h1>
<p>My CircuitPython assignment (Elisabeth Scharf)
The files in this repository are all CircuitPython assignments completed so far.
Completed:</p>
<ul>
<li>LED fade</li>
<li>Servo assignment</li>
<li>Photointerrupter</li>
<li>LCD screen</li>
<li>RGB and rgb</li>
</ul>
</article>
      </div>
  </div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">© 2019 <span title="0.31912s from unicorn-694b96df56-rw462">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com/">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com/">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com/" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com/" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://github.blog/" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-2e003yIUkuCG1IeaeQwIgzMwqYiC+7wN/ouvY2yay84wnLng3/MScKxudf02uj4T4RZAnF5zJumvacsF9lfTMw==" type="application/javascript" src="./hello_vs_code_files/frameworks-8e9b232b.js.download"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-7neFShGijgm1hfwoVdkflH5niCP1Al20ktUCrIVHN70YnuaKuLk76NwmHKx9l/0uJ0HMP6fCAnGbPk+M7asrIg==" type="application/javascript" src="./hello_vs_code_files/github-bootstrap-2775d2ae.js.download"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden="">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"></path></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="https://github.com/escharf72/CircuitPython">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="https://github.com/escharf72/CircuitPython">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog"></template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  


</body></html>