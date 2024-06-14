import useCompanyDataHook from '../../../features/customHooks/useCompanyDataHook.js';

const Header = () => {
  const { companyName, error } = useCompanyDataHook();
  return error ? <div>{error}</div> : companyName && <div>{companyName}</div>;
};

export default Header;
