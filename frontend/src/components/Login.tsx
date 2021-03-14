import React from 'react';
import { Formik, Field, Form, FormikHelpers } from 'formik';

interface LoginFields {
    email: string;
    password: string;
}

const Login = () =>  {
    return (
        <div className="login">
            <h1>Login Form</h1>
            <Formik
                initialValues={{ email: '', password: '' }}
                validate={values => {
                    const errors = {
                        email: ''
                    };
                    if (!values.email) {
                        errors.email = 'Required';
                    } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
                        errors.email = 'Invalid email address';
                    }
                    return errors;
                }}
                onSubmit={(
                    values: LoginFields, 
                    { setSubmitting }: FormikHelpers<LoginFields>
                ) => {
                    setTimeout(() => {
                        alert(JSON.stringify(values, null, 2));
                        setSubmitting(false);
                    }, 400);
                }}
                >
                    {({
                        values,
                        errors,
                        touched,
                        handleChange,
                        handleBlur,
                        handleSubmit,
                        isSubmitting
                    }) => (
                        <form onSubmit={handleSubmit}>
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                name="email"
                                id="email"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.email}
                            />
                            <br />
                            {errors.email && touched.email && errors.email}
                            <br />
                            <label htmlFor="password">Password</label>
                            <input 
                                type="password"
                                name="password"
                                id="password"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.password}
                            />
                            <br />
                            {errors.password && touched.password && errors.password}
                            <br />
                            <button type="submit" disabled={isSubmitting}>
                                Login
                            </button>
                        </form>
                    )}
            </Formik>
        </div>
    )
}

export default Login