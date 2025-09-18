<script lang="ts">
  import {
    Navbar,
    DarkMode,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
    Avatar,
    Dropdown,
    DropdownItem,
    DropdownHeader,
    DropdownGroup,
    Button,
  } from "flowbite-svelte";
  import logoDark from "$lib/assets/GitGudStats_logo_dark.svg";
  import logoLight from "$lib/assets/GitGudStats_logo_light.svg";

  import { isAuth } from "./stores/auth";
</script>

<Navbar class="bg-header-bg">
  <NavBrand href="/">
    <img src={logoDark} class="h-6 sm:h-9 dark:hidden" alt="GitGudStats Logo" />
    <img
      src={logoLight}
      class="h-6 sm:h-9 hidden dark:block"
      alt="GitGudStats Logo"
    />
    <span class="self-center font-semibold text-xl whitespace-nowrap ml-3"
      >GitGudStats</span
    >
  </NavBrand>

  <DarkMode class="mr-5 ml-auto hover:cursor-pointer"></DarkMode>

  {#if $isAuth}
    <div class="flex items-center md:order-2 hover:cursor-pointer">
      <!-- <Avatar id="avatar-menu" src="/user_pfp.jpeg" class="hover:cursor-pointer"/> -->
      <Avatar
      id="avatar-menu"
      src="https://media.licdn.com/dms/image/v2/D4D03AQEKpb81QDXHgA/profile-displayphoto-shrink_200_200/B4DZTWbbvcGkAc-/0/1738764305144?e=2147483647&v=beta&t=uwplIo_d4M5Ho0q3udJV5LJ7UbzigeT8zyRthdKEQ9M"
      border size="sm" class="focus:ring-primary-500 dark:focus:ring-primary-500 dark:bg-black" />
      <Dropdown placement="bottom" triggeredBy="#avatar-menu">
        <DropdownHeader class="hover:cursor-pointer">
          <span class="block text-sm">Pepe Gutierrez</span>
          <span class="block font-medium text-sm truncate">pepe81</span>
        </DropdownHeader>
        <DropdownGroup>
          <DropdownItem>Charts</DropdownItem>
          <DropdownItem>Settings</DropdownItem>
          <DropdownItem>Legal</DropdownItem>
        </DropdownGroup>
        <DropdownHeader>Sign out</DropdownHeader>
      </Dropdown>
      <!-- <NavHamburger /> This will display the NavUl -->
    </div>
  {/if}
  {#if !$isAuth}
    <a href="/login"> <Button outline>LOGIN</Button></a>
  {/if}

  <!-- From here to bottom are some useful stuff for maybe later -->

  <!-- <NavUl> These are header buttons, leave them just in case you want to reimplement them.
    <NavLi href="/">Home</NavLi>
    <NavLi href="/about">About</NavLi>
    <NavLi href="/docs/components/navbar">Navbar</NavLi>
    <NavLi href="/pricing">Pricing</NavLi>
    <NavLi href="/contact">Contact</NavLi>
  </NavUl> -->
  <!-- <Dropdown placement="bottom" triggeredBy="#avatar-menu">
    <DropdownHeader class="hover:cursor-pointer">
      <span class="block text-sm">Pepe Gutierrez</span>
      <span class="block font-medium text-sm truncate">pepe81</span>
    </DropdownHeader>
    <DropdownGroup>
      <DropdownItem>Charts</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Legal</DropdownItem>
    </DropdownGroup>
    <DropdownHeader>Sign out</DropdownHeader>
  </Dropdown> -->
</Navbar>
