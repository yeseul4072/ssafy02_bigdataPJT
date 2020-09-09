# Nuxt.js 정리

---

## Nuxt.js 의 사용 이유

> **"Vue.js 애플리케이션 개발을 보다 강력하고 사용하기 쉽게 만들어주는 프레임워크"**

- vue, router, vuex 와 같은 공식 라이브러리와 webpack, Babel, PostCSS를 기반으로 하여 Vue에서 하나하나 추가해야할 부분을 전체적으로 묶어주는 느낌인듯 하다

    → 즉, 개발자가 해야할 **설정을 상당수 줄여준다.**

- 특징정리

    [소개](https://ko.nuxtjs.org/guide#%ED%8A%B9%EC%A7%95)

- 서버와 클라이언트측 양쪽에서 실행할 수 있는 **범용 앱을 간단하게 만들어준다**

    → 서버까지도 한 프로젝트에서 진행이 가능 하다 : API도 한 프로젝트에서 만들어서 사용할 수 있는듯 하다.

- 일반적인 SPA로 개발하게 되면 검색엔진에서 조회 될 일이 없다.

    그러나 **SSR(Server Side Rendering)**으로 구성된 Nuxt를 사용한다면 서버렌더링으로 화면을 보여주게 되어 검색엔진 봇들이 페이지의 화면을 잘 긁어 갈 수 있다.

    → 옆에 사진에서 CSR(Client Side Rendering)과 SSR간에는 `Build Page` 단계가 어디에 있느냐에 대한 차이가 있다.

![resouce/Untitled.png](resouce/Untitled.png)

- 각 경로(page)에 대해 자동으로 코드가 분리되어 미리 렌더링 된 페이지를 가진다. **파일의 크기를 작게 유지**하므로 속도에 크게 도움이 된다
- React 의 Next.js에서 파생된 프레임워크
- Nuxt.js를 위한 라이브러리, 모듈                       `항상 모듈 다운받게되면 --save 사용하기`

    [Nuxt Community](https://github.com/nuxt-community)


## 라우팅

---

> Vue 에서는 vue-router를 시용해서 직접(수동)으로 추가해야한다.
그렇지만 Nuxt.js 에서는 `pages` 에서 자동으로 라우터 구성을 생성한다.
즉, 라우터 구성을 다시 작성할 필요가없다.

- 예시

**디렉토리 구조**

```jsx
pages/
--| user/
-----| index.vue
-----| one.vue
--| index.vue
```

**생성된 라우터 구성** 

```jsx
router: {
  routes: [
    {
      name: 'index',
      path: '/',
      component: 'pages/index.vue'
    },
    {
      name: 'user',
      path: '/user',
      component: 'pages/user/index.vue'
    },
    {
      name: 'user-one',
      path: '/user/one',
      component: 'pages/user/one.vue'
    }
  ]
}
```

### ./Users/_id.vue

 파라미터가 있는 동적라우트를 정의하기위해 **앞에 밑줄이 붙은 .vue파일을 정의한다**

 (회원정보 페이지나 게시판 조회등의 설계가 가능할듯)

```jsx
//**자동생성된 router 형식**
{
  name: 'users-id',
  path: '/users/:id?',
  component: 'pages/users/_id.vue'
},
```

사용된 매개변수는 validate()메소드를 통해 유효성 검사가 가능하다

```jsx
<script>
export default {
  validate(data) {
    // 라우트 매개변수 ID 값이 숫자인 경우만 허용
    return /^\d+$/.test(this.$route.params.id);
  }
};
</script>
```

**중첩라우팅**

디렉토리와 동일한 이름의 Vue 파일을 만들어서 설정한다.

자동으로 라우터가 잘 생성되는데 굳이 index파일을 만들어가며 사용하는 용도는 자식컴포넌트들에 동일한 작업을 부모에서 처리하고 넘겨주거나 할 때 사용하는것 같다.

`<nuxt-child />` 를 사용하여 내부에 자식 컴포넌트를 중첩시킨다.

![resouce/Untitled%203.png](resouce/Untitled%203.png)

```jsx
//pages/users.vue
<template>
  <nuxt-link to="/yamoo9">야무<nuxt-link>
  <nuxt-child />
</template>
```

## Axios / Proxy

---

> 브라우저에서 axios로 http요청을 보낼때 **CORS 에러**가 발생함.

 NPM 설치 및 nuxt.config.js로 import 작업

```jsx
$ npm i @nuxtjs/axios
$ npm i @nuxtjs/proxy
```

```jsx
module.exports = {
    modules: [
        '@nuxtjs/axios'
    ],
    axios: {
        proxy: true     // proxy 사용
    },
    proxy: {
        '/prefix-url': 'proxy-url'    // proxy url
    }
}
```