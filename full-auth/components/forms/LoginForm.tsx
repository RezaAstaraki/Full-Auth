"use client";

import React from "react";
import { Form } from "@/components/forms";
import { useLogin } from "@/hooks";
import { link } from "fs";
const LoginForm = () => {
  const { email, password, isLoading, onChange, onSubmit } = useLogin();

  const config = [
    {
      labelText: "Email Address",
      labelId: "email",
      type: "email",
      value: email,
      required: true,
    },
    {
      labelText: "Password",
      labelId: "password",
      type: "password",
      value: password,
      required: true,
      link: {
        linkText: "Forgot Password?",
        linkUrl: "/password-reset",
      },
    },
  ];

  return (
    <Form
      config={config}
      isLoading={isLoading}
      btnText="Sign In"
      onChange={onChange}
      onSubmit={onSubmit}
    />
  );
};

export default LoginForm;
