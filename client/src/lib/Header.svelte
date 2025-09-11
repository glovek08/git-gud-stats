<script lang="ts">
  import { Navbar, NavBrand, NavHamburger, NavUl, NavLi, Button } from "flowbite-svelte";
</script>

<header>
  <Navbar>
    <NavBrand href="/">
      <img src="/GitGudStats_logo_dark.png" class="mr-4 h-6 sm:h-9" alt="Flowbite Logo" />
      <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">GitGud Stats</span>
    </NavBrand>
    <div class="flex items-center lg:order-2">
      <Button href="/" color="dark" id="login-with-github-btn">Login with
        <img src="/GitHub_Logo_White.png" class="ml-1" alt="Log in with GitHub" height=40 width=60>
      </Button>
      <NavHamburger />
    </div>
    <!-- <NavUl>
      <NavLi href="/">HOME</NavLi>
    </NavUl> -->
  </Navbar>
</header>

